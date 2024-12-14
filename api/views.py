from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Company, Document, Signer, SignatureStatus
from .serializers import CompanySerializer, CreateDocumentSerializer, CreateSignerSerializer, ListDocumentSerializer
from .errors.erros import ErrosMessageEnum

from .repositories.document import DocumentRepository
from .repositories.company import CompanyRepository
from .repositories.zapsign import ZapSignRepository
from .repositories.signer import SignerRepository

@api_view(['GET'])
def get_documents(request, company_id):
    try:
        CompanyRepository.get_company(company_id)
        documents = DocumentRepository.get_documents_by_company(company_id)
        serializer = ListDocumentSerializer(documents, many=True)
        return Response(serializer.data)
    except Company.DoesNotExist:
        return Response({
               'error_code': ErrosMessageEnum.COMPANY_NOT_FOUND,
               'friendly_error_message': 'Empresa informada não existe'
            }, 
            status=status.HTTP_404_NOT_FOUND
        )

@api_view(['POST'])
def create_document(request):
    try:
        documentRequest = request.data.get('document')
        signersRequest = request.data.get('signers')

        documentSerializer = CreateDocumentSerializer(data=request.data.get('document'))
        documentSignersSerializer = CreateSignerSerializer(data=request.data.get('signers'), many=True)

        if not documentSignersSerializer.is_valid():
            return Response(documentSignersSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if not documentSerializer.is_valid():
            return Response(documentSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

        company = CompanyRepository.get_company(documentRequest.get('company'))
            
        signResponse = ZapSignRepository.sign_document_from_url(documentRequest.get('name'), documentRequest.get('url'), signersRequest, 'pt-br')
        if 'error' in signResponse:
            return Response({
                    'error_code': ErrosMessageEnum.DOCUMENT_NOT_CREATED,
                    'friendly_error_message': 'Ocorreu um erro ao enviar seu documento para assinatura eletrônica', 
                    'service': 'zapsign' 
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        documentToCreate = {
            'name': documentRequest.get('name'),
            'company': company,
            'open_id': signResponse.get('open_id'),
            'token': signResponse.get('token'),
            'created_by': signResponse.get('created_by')['email']
        }

        document = DocumentRepository.create_document(documentToCreate)

        signers_to_create = [
            Signer(
                document= document.instance,
                name= signer.get('name'),
                email= signer.get('email'),
                token= signer.get('token')
            )
            for signer in signResponse.get('signers')
        ]
        
        SignerRepository.create_many_document_signers(signers_to_create)
            
        return Response(document.data, status=status.HTTP_201_CREATED)
    except Company.DoesNotExist:
        return Response({
                    'error_code': ErrosMessageEnum.COMPANY_NOT_FOUND, 
                    'friendly_error_message': 'Empresa informada não existe'
                }, 
                status=status.HTTP_404_NOT_FOUND
            )
    except Exception as e:
        return Response({
                    'error_code': ErrosMessageEnum.INTERNAL_SERVER_ERROR, 
                    'friendly_error_message': 'Ocorreu um erro ao criar o documento',
                }, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
@api_view(['POST'])
def handle_webhook(request):
    try:
        event_type = request.data.get('event_type')
        print(f"""Event type: {event_type} has been received from webhook""")
        if event_type == 'doc_signed':
            # update signer status
            signerToken = request.data.get('signer_who_signed')['token']
            signer = SignerRepository.get_signer_from_token(signerToken)
            signer.status = SignatureStatus.SIGNED

            # update document status
            documentToken = request.data.get('token')
            document = DocumentRepository.get_document_by_token(documentToken)
            document.status = request.data.get('status').upper()

            signer.save()
            document.save()
        return Response(status=status.HTTP_200_OK)
    except Document.DoesNotExist:
        return Response({
                    'error_code': ErrosMessageEnum.DOCUMENT_NOT_FOUND, 
                    'friendly_error_message': 'Documento não encontrado'
                }, 
                status=status.HTTP_404_NOT_FOUND
            )
    except Exception as e:
        return Response({
                    'error_code': ErrosMessageEnum.INTERNAL_SERVER_ERROR, 
                    'friendly_error_message': 'Ocorreu um erro ao processar o webhook',
                }, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )