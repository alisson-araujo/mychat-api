from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.get_user import GetUser as GetUserInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse


class GetUsersController(ControllerInterface):
    def __init__(self, use_case: GetUserInterface):
        self.use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        list_phone_number = http_request.body["list_phone_number"]

        response = self.use_case.get_users(list_phone_number)

        return HttpResponse(status_code=200, body={"data": response})
