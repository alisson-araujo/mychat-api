from ..get_participants_controller import GetParticipantsController
from src.data.use_cases.get_participants import GetParticipants
from src.db.repositories.conversation_participants_repository import (
    CvsParticipantsRepository,
)


class HttpRequestMock:
    def __init__(self) -> None:
        self.query_params = {"conversation_id": 1}


def test_get_participants():
    request_mock = HttpRequestMock()
    use_case = GetParticipants(CvsParticipantsRepository)
    controller = GetParticipantsController(use_case)

    response = controller.handle(request_mock)

    assert response.status_code == 200
