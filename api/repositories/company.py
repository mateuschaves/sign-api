from abc import ABC, abstractmethod
from api.models import Company

class CompanyRepositoryInterface(ABC):
    @abstractmethod
    def get_company(company_id: int):
        pass

    @abstractmethod
    def save_document(company: Company):
        pass

class CompanyRepository(CompanyRepositoryInterface):
    def get_company(company_id: int):
        return Company.objects.get(id=company_id)
