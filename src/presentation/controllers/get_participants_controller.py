from src.presentation.http_types.http_response import HttpResponse
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.get_participants import (
    GetParticipants as GetParticipantsInterface,
)


class GetParticipantsController(ControllerInterface):
    def __init__(self, use_case: GetParticipantsInterface):
        self.use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        conversation_id = http_request.query_params["conversation_id"]

        response = self.use_case.get_participants(conversation_id)

        return HttpResponse(status_code=200, body={"data": response})
