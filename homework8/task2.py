import sqlite3
from typing import Iterable, Tuple


class TableData:
    """
    A wrapper class for database table, that,
    when initialized with database name and table,
    acts as collection object (implements Collection protocol).
    """
    def __init__(self, database_name: str, table_name: str):
        self.database_name = database_name
        self.table_name = table_name

        self.conn = sqlite3.connect(self.database_name)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def __len__(self) -> int:
        """Gives current amount of rows in presidents table in database."""
        return self.cursor.execute(f'SELECT COUNT(*) '
                                   f'from {self.table_name}').fetchone()[0]

    def __getitem__(self, item: str) -> Tuple[str]:
        """If an item is a table header, returns all values in it.
        If an item is a value, returns single data row
        from table_name if there is an item in it.
        """
        self.cursor.execute(f"SELECT * from {self.table_name} "
                            f"WHERE author=:item", {'item': item})
        return tuple(self.cursor.fetchone())

    def __contains__(self, item: str) -> bool:
        """Returns True if an item in a table."""
        self.cursor.execute(f"SELECT * from {self.table_name} "
                            f"WHERE author=:item", {'item': item})
        if tuple(self.cursor.fetchone()):
            return True

    def __iter__(self) -> Iterable:
        """Implements iteration protocol."""
        return iter(self.cursor.execute(f'SELECT * from {self.table_name}'))

    def __enter__(self) -> 'TableData':
        return self

    def __exit__(self, ext_type, exc_value, traceback) -> None:
        self.cursor.close()
        self.conn.close()
