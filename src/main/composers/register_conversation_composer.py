from src.db.repositories.conversation_repository import ConversationRepository
from src.data.use_cases.register_conversation import RegisterConversation
from src.presentation.controllers.register_conversation_controller import (
    RegisterConversationController,
)


def register_conversation_composer():
    repository = ConversationRepository()
    use_case = RegisterConversation(repository)
    controller = RegisterConversationController(use_case)

    return controller.handle
