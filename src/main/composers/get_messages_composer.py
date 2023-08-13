from src.db.repositories.message_repository import MessageRepository
from src.data.use_cases.get_messages import GetMessages
from src.presentation.controllers.get_messages_controller import GetMessagesController


def get_messages_composer():
    repository = MessageRepository()
    use_case = GetMessages(repository)
    controller = GetMessagesController(use_case)

    return controller.handle
