# from typing import Dict
from src.domain.use_cases.register_conversation import (
    RegisterConversation as RegisterConversationInterface,
)
from ..interfaces.conversation_repository import ConversationRepositoryInterface
from src.errors.types import HttpBadRequestError


class RegisterConversation(RegisterConversationInterface):
    def __init__(
        self, conversation_repository: ConversationRepositoryInterface
    ) -> None:
        self.conversation_repository = conversation_repository

    def register(self, name: str) -> int:
        self.__validate_name(name)
        id = self.conversation_repository.insert_conversation(name)
        return id

    @classmethod
    def __validate_name(cls, name: str) -> None:
        if name is None:
            raise HttpBadRequestError("Name is required")

        if len(name) > 20:
            raise HttpBadRequestError("Name is too long")
