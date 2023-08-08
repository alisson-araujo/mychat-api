from ..get_user_controller import GetUserController
from src.data.use_cases.get_user import GetUser
from src.db.repositories.user_repository import UserRepository
from src.presentation.http_types.http_response import HttpResponse


class HttpRequestMock:
    def __init__(self) -> None:
        self.query_params = {"phone_number": "5564992784886"}


def test_handle():
    request_mock = HttpRequestMock()
    use_case = GetUser(UserRepository)
    controller = GetUserController(use_case)

    response = controller.handle(request_mock)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
