from abc import ABC, abstractmethod
from src.db.entities.conversation import Conversation


class GetConversation(ABC):
    @abstractmethod
    def get_conversation_by_id(self, id: str) -> Conversation:
        pass
