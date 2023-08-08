from ..register_user_controller import RegisterUserController
from src.data.use_cases.register_user import RegisterUser
from src.db.repositories.user_repository import UserRepository
from src.presentation.http_types.http_response import HttpResponse
import pytest


class HttpRequestMock:
    def __init__(self) -> None:
        self.body = {
            "username": "Paul",
            "phone": "5564992784886",
            "password": "123456789",
        }


@pytest.mark.skip(reason="Sensitive test")
def test_register_user():
    request_mock = HttpRequestMock()
    use_case = RegisterUser(UserRepository)
    controller = RegisterUserController(use_case)

    response = controller.handle(request_mock)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 201
