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

    @abstractmethod
    def get_signer_from_token(token: str):
        pass

    @abstractmethod
    def remove_document_signer(signer_id: int):
        pass

class SignerRepository(SignerRepositoryInterface):
    def get_signers_from_document(document_id: int):
        return Signer.objects.filter(document_id=document_id)

    def create_document_signer(data: dict):
        return Signer.objects.create(**data)

    def create_many_document_signers(data: list):
        return Signer.objects.bulk_create(data)

    def get_signer_from_token(token: str):
        return Signer.objects.get(token=token)

    def remove_document_signer(signer_id: int):
        return Signer.objects.get(id=signer_id).delete()

    def update_document_signer(signer_id: int, data: dict):
        signer = Signer.objects.get(id=signer_id)
        for key, value in data.items():
            setattr(signer, key, value)
        signer.save()
        return signer