from src.infrastructure.manager_sqlite import ManagerSqlite
from src.infrastructure.repositories import UsersRepositorySqlite

SQLITE_PATH = "./database/database.sqlite"


def main():
    manager_sqlite = ManagerSqlite(SQLITE_PATH)
    users_repository = UsersRepositorySqlite(manager_sqlite)
    # users_repository.migration() # Uncomment to initialize the database
    users = users_repository.get_users()
    for user in users:
        print(user)


if __name__ == "__main__":
    main()
