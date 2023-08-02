from src.db.entities.message import Message
from abc import ABC, abstractmethod
from typing import List


class MessageRepositoryInterface(ABC):
    @abstractmethod
    def insert_message(self, conversation_id: int, user_id: int, content: str) -> int:
        pass

    @abstractmethod
    def get_message_by_conversation_id(self, conversation_id: int) -> List[Message]:
        pass