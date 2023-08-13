from fastapi import APIRouter, Request

from ..adapters.request_adapter import request_adapter
from ..composers.get_messages_composer import get_messages_composer
from ..composers.send_message_composer import send_message_composer
from src.presentation.http_types.http_request import HttpRequest

from src.errors.error_handler import handle_errors

router = APIRouter()


@router.get("/messages")
async def get_messages(request: Request):
    try:
        http_response = await request_adapter(request, get_messages_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return http_response


@router.post("/send-message")
async def send_message(request: Request):
    try:
        http_response = await request_adapter(request, send_message_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return http_response
