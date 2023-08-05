from src.db.repositories.conversation_repository import ConversationRepository
from .register_conversation import RegisterConversation


def test_register_cvs():
    mocked_name = "Jonas test"

    conversation_repository = ConversationRepository()
    register_conversation = RegisterConversation(conversation_repository)

    conversation = register_conversation.register(mocked_name)

    assert conversation is not None
