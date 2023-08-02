from abc import ABC, abstractmethod

class ConversationRepositoryInterface(ABC):
    @abstractmethod
    def insert_conversation(self, name: str) -> int:
        pass