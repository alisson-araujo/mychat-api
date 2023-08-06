from abc import ABC, abstractmethod
from src.db.entities.conversation import Conversation


class ConversationRepositoryInterface(ABC):
    @abstractmethod
    def insert_conversation(self, name: str) -> int:
        pass

    @abstractmethod
    def select_conversation_by_id(cls, id: int) -> Conversation:
        pass
