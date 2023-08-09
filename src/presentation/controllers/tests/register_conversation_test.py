from ..register_conversation_controller import RegisterConversationController
from src.data.use_cases.register_conversation import RegisterConversation
from src.db.repositories.conversation_repository import ConversationRepository
from src.presentation.http_types.http_response import HttpResponse
import pytest


class HttpRequestMock:
    def __init__(self) -> None:
        self.body = {
            "name": "Paul",
        }


@pytest.mark.skip(reason="Sensitive test")
def test_register_conversation():
    request_mock = HttpRequestMock()
    use_case = RegisterConversation(ConversationRepository)
    controller = RegisterConversationController(use_case)

    response = controller.handle(request_mock)
    assert isinstance(response, HttpResponse)
    assert response.status_code == 201
