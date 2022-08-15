from typing import Optional
from datetime import datetime


class Company:
    def __init__(self, name: str, ticker: str) -> None:
        creationg_date: datetime = datetime.now()

        # Common properties
        self.id: Optional[int] = None
        self.creation_date: datetime = creationg_date
        self.update_date: datetime = creationg_date

        # Specific properties
        self.name: str = name
        self.ticker: str = ticker
