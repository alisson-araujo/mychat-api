from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.register_user import RegisterUser as RegisterUserInterface


class RegisterUserController(ControllerInterface):
    def __init__(self, use_case: RegisterUserInterface):
        self.use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        username = http_request.body["username"]
        phone = http_request.body["phone"]
        password = http_request.body["password"]

        response = self.use_case.register(username, phone, password)

        return HttpResponse(status_code=201, body={"data": response})
