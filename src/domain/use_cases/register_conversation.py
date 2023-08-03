from abc import ABC, abstractmethod
from typing import Dict


class RegisterConversation(ABC):
    @abstractmethod
    def register(self, name: str) -> Dict:
        pass
