from abc import ABC, abstractmethod
from src.db.entities.user import User


class GetUser(ABC):
    @abstractmethod
    def get_user_by_phone(self, phone: str) -> User:
        pass
