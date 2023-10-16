from ...controllers.get_users_controller import GetUsersController
from src.data.use_cases.get_user import GetUser
from src.db.repositories.user_repository import UserRepository


class HttpRequestMock:
    def __init__(self) -> None:
        self.body = {"list_phone_number": ["+5511987654321", "+551198765"]}


def test_get_users():
    request_mock = HttpRequestMock()
    use_case = GetUser(UserRepository)
    controller = GetUsersController(use_case)

    response = controller.handle(request_mock)
    print(response.body)
    assert response.status_code == 200
    assert len(response.body["data"]) > 0
