from src.db.repositories.conversation_participants_repository import (
    CvsParticipantsRepository,
)
from src.data.use_cases.register_participant import RegisterParticipant
from src.presentation.controllers.register_participant_controller import (
    RegisterParticipantController,
)


def register_participant_composer():
    repository = CvsParticipantsRepository()
    use_case = RegisterParticipant(repository)
    controller = RegisterParticipantController(use_case)

    return controller.handle
