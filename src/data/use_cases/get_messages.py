from src.domain.use_cases.get_messages import GetMessages as GetMessagesInterface
from src.data.interfaces.message_repository import MessageRepositoryInterface
from src.db.entities.message import Message
from src.errors.types import HttpBadRequestError, HttpNotFoundError
from typing import List


class GetMessages(GetMessagesInterface):
    def __init__(self, message_repository: MessageRepositoryInterface) -> None:
        self.repository = message_repository

    def get_messages(self, cvs_id: int) -> List[Message]:
        self.__validate_id(cvs_id)

        messages = self.repository.get_message_by_conversation_id(cvs_id)
        if not messages:
            raise HttpNotFoundError("no messages found for this conversation")
        return messages

    def __validate_id(self, cvs_id: int) -> None:
        if not isinstance(cvs_id, int):
            raise HttpBadRequestError("conversation id must be an integer")

        if cvs_id <= 0:
            raise HttpBadRequestError("conversation id must be a positive integer")
