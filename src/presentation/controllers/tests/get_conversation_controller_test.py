from ..get_conversation_controller import GetConversationController
from src.data.use_cases.get_conversation import GetConversation
from src.db.repositories.conversation_repository import ConversationRepository


class HttpRequestMock:
    def __init__(self) -> None:
        self.body = {"id": 1}


def test_get_conversation():
    request_mock = HttpRequestMock()
    use_case = GetConversation(ConversationRepository)
    controller = GetConversationController(use_case)

    response = controller.handle(request_mock)

    assert response.status_code == 200
