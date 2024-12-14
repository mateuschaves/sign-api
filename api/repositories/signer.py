from abc import ABC, abstractmethod
from api.models import Signer
from api.serializers import ListDocumentSerializer

class SignerRepositoryInterface(ABC):
    @abstractmethod
    def get_signers_from_document(company_id: int):
        pass

    @abstractmethod
    def create_document_signer(data: dict):
        pass

    @abstractmethod
    def create_many_document_signers(data: list):
        pass

class SignerRepository(SignerRepositoryInterface):
    def get_signers_from_document(document_id: int):
        return Signer.objects.filter(document_id=document_id)

    def create_document_signer(data: dict):
        return Signer.objects.create(**data)

    def create_many_document_signers(data: list):
        return Signer.objects.bulk_create(data)