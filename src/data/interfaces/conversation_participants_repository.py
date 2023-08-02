from abc import ABC, abstractmethod
from src.db.entities.conversation_participants import CvsParticipants
from typing import List

class CvsParticipantsRepositoryInterface(ABC):
    @abstractmethod
    def insert_cvs_participant(self, conversation_id: int, user_id: int) -> int:
        pass

    @abstractmethod
    def get_cvs_participants_by_conversation_id(self, conversation_id: int) -> List[CvsParticipants]:
        pass
    