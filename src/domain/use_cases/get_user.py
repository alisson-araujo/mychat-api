from abc import ABC, abstractmethod
from src.db.entities.user import User
from typing import List


class GetUser(ABC):
    @abstractmethod
    def get_user_by_phone(self, phone: str) -> User:
        pass

    @abstractmethod
    def get_users(self, list_of_phones: list) -> List:
        pass
