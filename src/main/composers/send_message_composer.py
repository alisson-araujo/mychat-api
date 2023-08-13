from src.db.repositories.message_repository import MessageRepository
from src.data.use_cases.register_message import RegisterMessage
from src.presentation.controllers.register_message_controller import (
    RegisterMessageController,
)


def send_message_composer():
    repository = MessageRepository()
    use_case = RegisterMessage(repository)
    controller = RegisterMessageController(use_case)

    return controller.handle
