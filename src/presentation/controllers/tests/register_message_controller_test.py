from ..register_message_controller import RegisterMessageController
from src.data.use_cases.register_message import RegisterMessage
from src.db.repositories.message_repository import MessageRepository
import pytest


class HttpRequestMock:
    def __init__(self) -> None:
        self.body = {"conversation_id": 1, "user_id": 1, "content": "Hello World!"}


@pytest.mark.skip(reason="Sensitive test")
def test_register_message():
    request_mock = HttpRequestMock()
    use_case = RegisterMessage(MessageRepository)
    controller = RegisterMessageController(use_case)

    response = controller.handle(request_mock)
    print(response.body)
    assert response.status_code == 201
