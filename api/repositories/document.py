from abc import ABC, abstractmethod
from api.models import Document
from api.serializers import ListDocumentSerializer

class DocumentRepositoryInterface(ABC):
    @abstractmethod
    def get_document_by_id(id: int):
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

    @abstractmethod
    def get_documents():
        pass

class DocumentRepository(DocumentRepositoryInterface):
    def get_document_by_id(id: int):
        return Document.objects.prefetch_related('signers').prefetch_related('company').get(id=id)

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

    def get_documents():
        return Document.objects.all().prefetch_related('signers').prefetch_related('company').order_by('created_at')
