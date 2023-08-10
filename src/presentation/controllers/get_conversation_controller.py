from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.get_conversation import (
    GetConversation as GetConversationInterface,
)


class GetConversationController(ControllerInterface):
    def __init__(self, use_case: GetConversationInterface):
        self.use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        conversation_id = http_request.body["id"]

        response = self.use_case.get_conversation_by_id(conversation_id)

        return HttpResponse(status_code=200, body={"data": response})
