from src.db.repositories.conversation_repository import ConversationRepository
from src.data.use_cases.get_conversation import GetConversation
from src.presentation.controllers.get_conversation_controller import (
    GetConversationController,
)


def get_conversation_composer():
    repository = ConversationRepository()
    use_case = GetConversation(repository)
    controller = GetConversationController(use_case)

    return controller.handle
