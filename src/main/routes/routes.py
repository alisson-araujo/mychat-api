from fastapi import APIRouter, Request

from ..adapters.request_adapter import request_adapter
from ..composers.get_messages_composer import get_messages_composer

from src.errors.error_handler import handle_errors

router = APIRouter()


@router.get("/messages")
def get_messages(request: Request):
    try:
        http_response = request_adapter(request, get_messages_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return http_response
