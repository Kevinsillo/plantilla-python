from src.domain.users_repository import UsersRepository
from src.infrastructure.manager_sqlite import ManagerSqlite


class UsersRepositorySqlite(UsersRepository):
    """
    SQLite implementation of the UsersRepository interface
    """

    def __init__(self, manager_sqlite: ManagerSqlite):
        self.manager_sqlite = manager_sqlite

    def migration(self):
        query = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            surname TEXT NOT NULL,
            age TEXT NOT NULL,
            email TEXT NOT NULL
        );
        """
        self.manager_sqlite.execute_query(query)
        self.insert_user("Juan", "Perez", 30, "jperez@example.com")
        self.insert_user("Maria", "Gomez", 25, "mgomez@example.com")
        self.insert_user("Carlos", "Lopez", 35, "clopez@example.com")

    def get_users(self):
        query = """
        SELECT id, name, surname, age, email
        FROM users;
        """
        return self.manager_sqlite.fetch_all(query)

    def insert_user(self, name: str, surname: str, age: int, email: str):
        query = """
        INSERT INTO users (name, surname, age, email)
        VALUES (:name, :surname, :age, :email);
        """
        params = (name, surname, age, email)
        self.manager_sqlite.execute_query(query, params)
