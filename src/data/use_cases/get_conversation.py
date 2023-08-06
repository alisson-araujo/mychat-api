from src.domain.use_cases.get_conversation import (
    GetConversation as GetConversationInterface,
)
from src.data.interfaces.conversation_repository import ConversationRepositoryInterface
from src.errors.types import HttpNotFoundError, HttpBadRequestError
from src.db.entities.conversation import Conversation


class GetConversation(GetConversationInterface):
    def __init__(
        self, conversation_repository: ConversationRepositoryInterface
    ) -> None:
        self.conversation_repository = conversation_repository

    def get_conversation_by_id(self, id: str) -> Conversation:
        self.__validate_id(id)

        conversation = self.conversation_repository.select_conversation_by_id(id)
        if conversation is None:
            raise HttpNotFoundError("Conversation not found")
        return conversation

    def __validate_id(cls, id: int) -> None:
        if id is None:
            raise HttpBadRequestError("Conversation id is required")

        if not isinstance(id, int):
            raise HttpBadRequestError("Conversation id must be a number")
