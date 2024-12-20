from abc import ABC, abstractmethod


class UsersRepository(ABC):
    """
    Users repository interface
    """

    @abstractmethod
    def migration(self) -> None:
        """
        Initialize the database with some data
        """

    @abstractmethod
    def get_users(self) -> list[object]:
        """
        Get all users from the database

        return: List of users
        """

    @abstractmethod
    def insert_user(self, name: str, surname: str, age: int, email: str) -> None:
        """
        Insert a new user into the database

        param name: User's name
        param surname: User's surname
        param age: User's age
        param email: User's email
        """
