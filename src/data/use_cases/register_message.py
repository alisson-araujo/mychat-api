from typing import Dict
from src.domain.use_cases.register_message import (
    RegisterMessage as RegisterMessageInterface,
)
from src.data.interfaces.message_repository import MessageRepositoryInterface
from src.errors.types import HttpBadRequestError


class RegisterMessage(RegisterMessageInterface):
    def __init__(self, message_repository: MessageRepositoryInterface):
        self.message_repository = message_repository

    def register(self, conversation_id: int, user_id: int, content: str) -> int:
        self.__validate_content(content)

        message_id = self.message_repository.insert_message(
            conversation_id, user_id, content
        )

        return message_id

    def __validate_content(self, content: str) -> None:
        if not content:
            raise HttpBadRequestError("Content is required")

        if len(content) > 255:
            raise HttpBadRequestError("Content must be less than 255 characters")
