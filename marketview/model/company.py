from typing import Optional
from datetime import datetime


class Company:
    def __init__(
        self,
        id: Optional[int] = None,
        name: Optional[str] = None,
        ticker: Optional[str] = None
    ) -> None:
        creationg_date: datetime = datetime.now()

        # Common properties
        self.id: Optional[int] = id
        self.creation_date: datetime = creationg_date
        self.update_date: datetime = creationg_date

        # Specific properties
        self.name: Optional[str] = name
        self.ticker: Optional[str] = ticker
