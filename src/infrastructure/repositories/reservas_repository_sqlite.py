from src.domain.reservas_repository import ReservasRepository
from src.infrastructure.gestor_sqlite import GestorSqlite


class ReservasRepositorySqlite(ReservasRepository):
    """Repositorio de reservas en MySQL"""

    def __init__(self, gestor_sqlite: GestorSqlite):
        self.gestor_sqlite = gestor_sqlite

    def crear_tabla(self):
        print("Creando tabla de reservas")
        query = """
        CREATE TABLE IF NOT EXISTS reservas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            fecha_inicio TEXT NOT NULL,
            fecha_fin TEXT NOT NULL
        );
        """
        self.gestor_sqlite.execute_query(query)
        self.guardar_reserva("Juan", "2021-10-10", "2021-10-11")
        self.guardar_reserva("Pedro", "2021-10-12", "2021-10-13")
        self.guardar_reserva("María", "2021-10-14", "2021-10-15")

    def obtener_reservas(self):
        print("Obteniendo reservas")
        query = """
        SELECT id, nombre, fecha_inicio, fecha_fin
        FROM reservas;
        """
        return self.gestor_sqlite.fetch_all(query)

    def guardar_reserva(self, nombre: str, fecha_inicio: str, fecha_fin: str):
        print("Guardando reserva")
        query = """
        INSERT INTO reservas (nombre, fecha_inicio, fecha_fin)
        VALUES (?, ?, ?);
        """
        params = (nombre, fecha_inicio, fecha_fin)
        self.gestor_sqlite.execute_query(query, params)
