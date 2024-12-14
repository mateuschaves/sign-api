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

class DocumentRepository(DocumentRepositoryInterface):
    def get_documents_by_company(company_id: int):
        return Document.objects.filter(company_id=company_id)

    def create_document(data: dict):
        return ListDocumentSerializer(Document.objects.create(**data))

    def get_document_by_token(token: str):
        return Document.objects.get(token=token)
