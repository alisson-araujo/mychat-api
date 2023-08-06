from abc import ABC, abstractmethod
from src.db.entities.conversation_participants import CvsParticipants
from typing import List


class GetParticipants(ABC):
    @abstractmethod
    def get_participants(self, cvs_id: int) -> List[CvsParticipants]:
        pass
