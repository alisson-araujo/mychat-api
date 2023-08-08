from src.presentation.http_types.http_response import HttpResponse
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.get_user import GetUser as GetUserInterface


class GetUserController(ControllerInterface):
    def __init__(self, use_case: GetUserInterface):
        self.use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        phone_number = http_request.query_params["phone_number"]

        response = self.use_case.get_user_by_phone(phone_number)

        return HttpResponse(status_code=200, body={"data": response})
