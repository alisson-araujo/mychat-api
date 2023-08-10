from ..register_participant_controller import RegisterParticipantController
from src.data.use_cases.register_participant import RegisterParticipant
from src.db.repositories.conversation_participants_repository import (
    CvsParticipantsRepository,
)


class HttpRequestMock:
    def __init__(self) -> None:
        self.body = {"conversation_id": "1", "participant_id": "2"}


def test_register_participant():
    request_mock = HttpRequestMock()
    use_case = RegisterParticipant(CvsParticipantsRepository)
    controller = RegisterParticipantController(use_case)

    response = controller.handle(request_mock)
    print(response)
    assert response.status_code == 201
