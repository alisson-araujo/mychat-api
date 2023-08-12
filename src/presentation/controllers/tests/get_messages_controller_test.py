from ..get_messages_controller import GetMessagesController
from src.data.use_cases.get_messages import GetMessages
from src.db.repositories.message_repository import MessageRepository


class HttpRequestMock:
    def __init__(self) -> None:
        self.query_params = {"conversation_id": 1}


def test_get_messsages():
    request_mock = HttpRequestMock()
    use_case = GetMessages(MessageRepository)
    controller = GetMessagesController(use_case)

    response = controller.handle(request_mock)
    print(response.body)
    assert response.status_code == 200
