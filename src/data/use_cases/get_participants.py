from src.domain.use_cases.get_participants import (
    GetParticipants as GetParticipantsInterface,
)
from src.data.interfaces.conversation_participants_repository import (
    CvsParticipantsRepositoryInterface,
)
from src.db.entities.conversation_participants import CvsParticipants
from src.errors.types import HttpBadRequestError, HttpNotFoundError
from typing import List


class GetParticipants(GetParticipantsInterface):
    def __init__(
        self, cvs_participants_repository: CvsParticipantsRepositoryInterface
    ) -> None:
        self.repository = cvs_participants_repository

    def get_participants(self, cvs_id: int) -> List[CvsParticipants]:
        self.__validate_id(cvs_id)

        participants = self.repository.get_cvs_participants_by_conversation_id(cvs_id)
        if participants is None:
            raise HttpNotFoundError("Participants not found")
        return participants

    def __validate_id(cls, id: int) -> None:
        if id is None:
            raise HttpBadRequestError("Conversation id is required")

        if not isinstance(id, int):
            raise HttpBadRequestError("Conversation id must be a number")
