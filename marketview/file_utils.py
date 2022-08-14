import os
from pathlib import Path


def get_app_directory() -> str:
    return os.path.join(get_home_directory(), ".local/share/marketview/")


def get_home_directory() -> str:
    return str(Path.home())


def get_ticker_directory(ticker: str) -> str:
    return os.path.join(get_app_directory(), ticker)
