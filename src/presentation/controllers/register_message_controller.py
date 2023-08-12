from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.domain.use_cases.register_message import (
    RegisterMessage as RegisterMessageInterface,
)
from src.presentation.interfaces.controller_interface import ControllerInterface


class RegisterMessageController(ControllerInterface):
    def __init__(self, use_case: RegisterMessageInterface):
        self.use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        conversation_id = http_request.body["conversation_id"]
        user_id = http_request.body["user_id"]
        content = http_request.body["content"]

        response = self.use_case.register(conversation_id, user_id, content)

        return HttpResponse(status_code=201, body={"data": response})
