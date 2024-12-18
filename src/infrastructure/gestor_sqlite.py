import sqlite3


class GestorSqlite:
    """Clase para gestionar la conexión y consultas a una base de datos SQLite."""

    def __init__(self, db_path):
        """
        Inicializa la clase y establece una conexión con la base de datos SQLite.

        :param db_path: Path al archivo de la base de datos SQLite.
        """
        self.db_path = db_path
        self.conn = None
        self.cursor = None
        self.connect()

    def connect(self):
        """Establece la conexión con la base de datos."""
        try:
            self.conn = sqlite3.connect(self.db_path)
            self.conn.row_factory = sqlite3.Row
            self.cursor = self.conn.cursor()
            print("Conexión establecida con la base de datos.")
        except sqlite3.Error as e:
            print(f"Error al conectar con la base de datos: {e}")
            self.conn = None
            self.cursor = None

    def execute_query(self, query: str, params: object = None) -> None:
        """
        Ejecuta una consulta SQL (INSERT, UPDATE, DELETE).

        :param query: Consulta SQL a ejecutar.
        :param params: Parámetros para la consulta (opcional).
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

    def fetch_one(self, query: str, params: object = None) -> list:
        """
        Obtiene un solo resultado de una consulta SELECT.

        :param query: Consulta SELECT.
        :param params: Parámetros para la consulta (opcional).
        :return: Tupla con el resultado.
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

    def fetch_all(self, query: str, params: object = None) -> list:
        """
        Obtiene todos los resultados de una consulta SELECT.

        :param query: Consulta SELECT.
        :param params: Parámetros para la consulta (opcional).
        :return: Lista de resultados.
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

    def close(self):
        """Cierra la conexión con la base de datos."""
        if self.conn:
            self.conn.close()
            print("Conexión cerrada.")
