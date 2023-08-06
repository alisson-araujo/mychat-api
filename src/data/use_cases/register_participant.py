from src.domain.use_cases.register_participant import (
    RegisterParticipant as RegisterParticipantInterface,
)
from ..interfaces.conversation_participants_repository import (
    CvsParticipantsRepositoryInterface,
)
from src.errors.types import HttpBadRequestError


class RegisterParticipant(RegisterParticipantInterface):
    def __init__(
        self, cvs_participants_repository: CvsParticipantsRepositoryInterface
    ) -> None:
        self.cvs_participants_repository = cvs_participants_repository

    def register(self, conversation_id: int, user_id: int) -> int:
        if conversation_id is None or user_id is None:
            raise HttpBadRequestError("conversation_id and user_id are required")

        id = self.cvs_participants_repository.insert_cvs_participant(
            conversation_id, user_id
        )

        return id
