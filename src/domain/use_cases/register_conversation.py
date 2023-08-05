from abc import ABC, abstractmethod


class RegisterConversation(ABC):
    @abstractmethod
    def register(self, name: str) -> int:
        pass
