from typing import Any, Dict

from marketview.model.company import Company
from datetime import datetime


class CompanyRowMapper:

    def map_row(self, row: Dict[str, Any]) -> Company:
        company: Company = Company(name=row["name"], ticker=row["ticker"])
        company.id = row["id"]
        company.creation_date = datetime.fromisoformat(row["creation_date"])
        company.update_date = datetime.fromisoformat(row["update_date"])
        return company

    def map_entity(self, company: Company) -> Dict[str, Any]:
        row: Dict[str, Any] = {
            "id": company.id
        }

        return row
