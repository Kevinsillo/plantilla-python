from src.infrastructure.gestor_sqlite import GestorSqlite
from src.infrastructure.repositories import ReservasRepositorySqlite

SQLITE_PATH = "./database/reservas.sqlite"


def main():
    gestor_sqlite = GestorSqlite(SQLITE_PATH)
    reservas_repository = ReservasRepositorySqlite(gestor_sqlite)
    # reservas_repository.crear_tabla()
    reservas = reservas_repository.obtener_reservas()
    print(reservas)


if __name__ == "__main__":
    main()
