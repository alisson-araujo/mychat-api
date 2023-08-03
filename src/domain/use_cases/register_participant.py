from abc import ABC, abstractmethod
from typing import Dict


class RegisterParticipant(ABC):
    @abstractmethod
    def register(self, conversation_id: int, user_id: int) -> Dict:
        pass
