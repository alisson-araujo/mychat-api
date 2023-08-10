from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.domain.use_cases.register_participant import (
    RegisterParticipant as RegisterParticipantInterface,
)
from src.presentation.interfaces.controller_interface import ControllerInterface


class RegisterParticipantController(ControllerInterface):
    def __init__(self, use_case: RegisterParticipantInterface):
        self.use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        conversation_id = http_request.body["conversation_id"]
        participant_id = http_request.body["participant_id"]

        response = self.use_case.register(conversation_id, participant_id)

        return HttpResponse(status_code=201, body={"data": response})
