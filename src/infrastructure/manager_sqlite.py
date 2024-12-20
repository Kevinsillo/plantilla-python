import sqlite3


class ManagerSqlite:
    """
    Class to manage the connection and queries to a SQLite database.
    """

    def __init__(self, db_path):
        """
        Initializes the class and establishes a connection to the SQLite database.

        :param db_path: Path to the SQLite database file.
        """
        self.db_path = db_path
        self.conn = None
        self.cursor = None
        self.connect()

    def connect(self):
        """
        Establishes a connection to the SQLite database.
        """
        try:
            self.conn = sqlite3.connect(self.db_path)
            self.conn.row_factory = sqlite3.Row
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(f"Error connecting to the database: {e}")
            self.conn = None
            self.cursor = None

    def execute_query(self, query: str, params: object = None) -> None:
        """
        Excecute a SQL query (INSERT, UPDATE, DELETE).

        :param query: SQL query.
        :param params: Parameters for the query (optional).
        :return: None
        """
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error ejecutando la consulta: {e}")

    def fetch_one(self, query: str, params: object = None) -> object:
        """
        Get a single result from a SELECT query.

        :param query: SQL query.
        :param params: Parameters for the query (optional).
        :return: Single result.
        """
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            row = self.cursor.fetchone()
            return dict(row) if row else []
        except sqlite3.Error as e:
            print(f"Error al obtener datos: {e}")
            return []

    def fetch_all(self, query: str, params: object = None) -> list[object]:
        """
        Get a list of results from a SELECT query.

        :param query: SQL query.
        :param params: Parameters for the query (optional).
        :return: List of results.
        """
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return [dict(row) for row in rows] if rows else []
        except sqlite3.Error as e:
            print(f"Error al obtener datos: {e}")
            return []

    def __del__(self):
        """
        Closes the connection to the SQLite database.
        """
        if self.conn:
            self.conn.close()
