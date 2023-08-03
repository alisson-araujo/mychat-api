from abc import ABC, abstractmethod
from typing import Dict


class RegisterUser(ABC):
    @abstractmethod
    def register(self, username: str, phone: str, password: str) -> Dict:
        pass
