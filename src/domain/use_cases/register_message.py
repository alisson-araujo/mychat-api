from abc import ABC, abstractmethod
from typing import Dict


class RegisterMessage(ABC):
    @abstractmethod
    def register(self, conversation_id: int, user_id: int, content: str) -> int:
        pass
