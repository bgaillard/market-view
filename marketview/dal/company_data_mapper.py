from sqlite3 import Cursor, Row
from typing import Optional

from marketview.dal.company_row_mapper import CompanyRowMapper
from marketview.dal.data_mapper import get_cursor
from marketview.model.company import Company


class CompanyDataMapper:
    def __init__(self) -> None:
        self.row_mapper: CompanyRowMapper = CompanyRowMapper()

    def find_by_id(self, id: int) -> Optional[Company]:
        row: Optional[Row] = get_cursor().execute(
            "select * from company where id=:id",
            {
                "id": id
            }
        ).fetchone()

        return None if not row else self.row_mapper.map_row(row=dict(row))

    def save(self, company: Company) -> Company:
        cursor: Cursor = get_cursor().execute(
            (
                "insert into company(creation_date, update_date, name, ticker) "
                "values(:creation_date, :update_date, :name, :ticker)"
            ),
            self.row_mapper.map_entity(company)
        )
        row: Row = cursor.fetchone()

        company.id = row.id["id"]  # type: ignore
        return company
