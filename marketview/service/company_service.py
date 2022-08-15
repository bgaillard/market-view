from marketview.model.company import Company
from marketview.dal.company_data_mapper import CompanyDataMapper
from marketview.dal.data_mapper import transactional

from typing import Optional


class CompanyService:
    def __init__(self) -> None:
        self.company_data_mapper = CompanyDataMapper()

    def find_by_id(self, id: int) -> Optional[Company]:
        return self.company_data_mapper.find_by_id(id=id)

    @transactional
    def save(self, company: Company) -> Company:
        return self.company_data_mapper.save(company=company)
