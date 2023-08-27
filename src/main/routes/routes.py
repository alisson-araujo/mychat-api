from fastapi import APIRouter, Request

from ..adapters.request_adapter import request_adapter
from ..composers.get_messages_composer import get_messages_composer
from ..composers.send_message_composer import send_message_composer
from ..composers.get_user_composer import get_user_composer
from ..composers.get_conversation_composer import get_conversation_composer
from ..composers.register_conversation_composer import register_conversation_composer
from ..composers.get_participants_composer import get_participants_composer
from ..composers.register_participants_controller import register_participant_composer

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


@router.get("/user")
async def get_user(request: Request):
    try:
        http_response = await request_adapter(request, get_user_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return http_response


@router.get("/conversation")
async def get_conversation(request: Request):
    try:
        http_response = await request_adapter(request, get_conversation_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return http_response


@router.post("/register-conversation")
async def register_conversation(request: Request):
    try:
        http_response = await request_adapter(request, register_conversation_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return http_response


@router.get("/participants")
async def get_participants(request: Request):
    try:
        http_response = await request_adapter(request, get_participants_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return http_response


@router.post("/register-participant")
async def register_participant(request: Request):
    try:
        http_response = await request_adapter(request, register_participant_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return http_response
