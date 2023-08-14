from src.db.repositories.conversation_participants_repository import (
    CvsParticipantsRepository,
)
from src.data.use_cases.get_participants import GetParticipants
from src.presentation.controllers.get_participants_controller import (
    GetParticipantsController,
)


def get_participants_composer():
    repository = CvsParticipantsRepository()
    use_case = GetParticipants(repository)
    controller = GetParticipantsController(use_case)

    return controller.handle
