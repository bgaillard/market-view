from sqlite3 import Cursor, Row
from typing import Optional

from marketview.dal.day_point_close_row_mapper import DayPointCloseRowMapper
from marketview.dal.data_mapper import get_cursor
from marketview.model.day_point_close import DayPointClose


class DayPointCloseDataMapper:
    def __init__(self) -> None:
        self.row_mapper: DayPointCloseRowMapper = DayPointCloseRowMapper()

    def find_by_id(self, id: int) -> Optional[DayPointClose]:
        row: Optional[Row] = get_cursor().execute(
            "select * from day_point_close where id=:id",
            {
                "id": id
            }
        ).fetchone()

        return None if not row else self.row_mapper.map_row(row=dict(row))

    def save(self, day_point_close: DayPointClose) -> DayPointClose:
        cursor: Cursor = get_cursor().execute(
            (
                "insert into day_point_close(creation_date, update_date, name, ticker) "
                "values(:creation_date, :update_date, :name, :ticker)"
            ),
            self.row_mapper.map_entity(day_point_close)
        )
        row: Row = cursor.fetchone()

        day_point_close.id = row.id["id"]  # type: ignore
        return day_point_close
