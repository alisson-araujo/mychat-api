from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.register_conversation import (
    RegisterConversation as RegisterConversationInterface,
)


class RegisterConversationController(ControllerInterface):
    def __init__(self, use_case: RegisterConversationInterface):
        self.use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        name = http_request.body["name"]

        response = self.use_case.register(name)

        return HttpResponse(status_code=201, body={"data": response})
