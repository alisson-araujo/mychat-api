from abc import ABC, abstractmethod
from src.db.entities.user import User


class UserRepositoryInterface(ABC):
    @abstractmethod
    def insert_user(self, user: User) -> int:
        pass

    @abstractmethod
    def get_user_by_phone(self, phone: str) -> User:
        pass
