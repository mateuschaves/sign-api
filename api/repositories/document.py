from abc import ABC, abstractmethod
from api.models import Document
from api.serializers import ListDocumentSerializer

class DocumentRepositoryInterface(ABC):
    @abstractmethod
    def get_documents_by_company(company_id: int):
        pass

    @abstractmethod
    def create_document(data: dict):
        pass

    @abstractmethod
    def get_document_by_token(token: str):
        pass

    @abstractmethod
    def remove_document(document_id: int):
        pass

    @abstractmethod
    def update_document(document_id: int, data: dict):
        pass

class DocumentRepository(DocumentRepositoryInterface):
    def get_documents_by_company(company_id: int):
        return Document.objects.filter(company_id=company_id).prefetch_related('signers')

    def create_document(data: dict):
        return ListDocumentSerializer(Document.objects.create(**data))

    def get_document_by_token(token: str):
        return Document.objects.get(token=token)

    def remove_document(document_id: int):
        return Document.objects.get(id=document_id).delete()

    def update_document(document_id: int, data: dict):
        document = Document.objects.get(id=document_id)
        for key, value in data.items():
            setattr(document, key, value)
        document.save()
        return document
