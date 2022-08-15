from typing import Callable, Optional
import sqlite3
from sqlite3 import Connection, Cursor, Row

connection: Optional[Connection] = None


def get_connection() -> Connection:
    global connection

    if not connection:
        connection = sqlite3.connect(database="marketview.db")
        connection.row_factory = Row

    return connection


def get_cursor() -> Cursor:
    return get_connection().cursor()


def transactional(func) -> Callable:
    def wrapper(*args, **kwargs) -> None:
        connection: Connection = get_connection()

        func(*args, **kwargs)

        connection.commit()
        connection.close()

    return wrapper
