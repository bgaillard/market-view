from datetime import datetime
from typing import Optional

from marketview.model.company import Company


class DayPointClose:
    def __init__(
        self,
        id: Optional[int] = None,
        date: Optional[datetime] = None,
        value: Optional[float] = None,
        company: Optional[Company] = None
    ) -> None:
        self.id: Optional[int] = id
        self.date: Optional[datetime] = date
        self.value: Optional[float] = value
        self.company: Optional[Company] = company
