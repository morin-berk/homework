import sqlite3


class TableData:
    """
    A wrapper class for database table, that,
    when initialized with database name and table,
    acts as collection object (implements Collection protocol).
    """
    def __init__(self, database_name: str, table_name: str):
        self.database_name = database_name
        self.table_name = table_name

        conn = sqlite3.connect(self.database_name)
        conn.row_factory = sqlite3.Row
        self.cursor = conn.cursor()

    def __len__(self) -> int:
        """Gives current amount of rows in presidents table in database."""
        counter = 0
        for _ in self.cursor.execute(f'SELECT * from {self.table_name}'):
            counter += 1
        return counter

    def __getitem__(self, item: str):
        """If an item is a table header, returns all values in it.
        If an item is a value, returns single data row
        from table_name if there is an item in it.
        """
        for row in self.cursor.execute(f"SELECT * from {self.table_name}"):
            if item in row:
                return tuple(row)
            elif item in row.keys():
                return row[item]

    def __contains__(self, item):
        """Returns True if an item in a table."""
        for row in self.cursor.execute(f'SELECT * from {self.table_name}'):
            if item in row:
                return True

    def __iter__(self) -> sqlite3.Row:
        """Implements iteration protocol."""
        for row in self.cursor.execute(f'SELECT * from {self.table_name}'):
            yield row
