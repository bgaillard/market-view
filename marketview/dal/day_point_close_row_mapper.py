from datetime import datetime
from typing import Any, Dict

from marketview.model.company import Company
from marketview.model.day_point_close import DayPointClose


class DayPointCloseRowMapper:

    def map_row(self, row: Dict[str, Any]) -> DayPointClose:
        day_point_close: DayPointClose = DayPointClose()
        day_point_close.id = row["id"]
        day_point_close.date = datetime.fromisoformat(row["date"])
        day_point_close.value = row["value"]

        company: Company = Company()
        company.id = row["company_id"]
        day_point_close.company = company

        return day_point_close

    def map_entity(self, day_point_close: DayPointClose) -> Dict[str, Any]:
        row: Dict[str, Any] = {
            "id": day_point_close.id
        }

        return row
