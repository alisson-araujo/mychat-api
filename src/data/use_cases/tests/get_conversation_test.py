from src.db.repositories.conversation_repository import ConversationRepository
from ..get_conversation import GetConversation
from src.db.entities.conversation import Conversation


def test_get_conversation():
    mocked_conversation_id = 1
    conversation_repository = ConversationRepository()
    get_conversation = GetConversation(conversation_repository)

    conversation = get_conversation.get_conversation_by_id(mocked_conversation_id)

    assert conversation is not None
    assert isinstance(conversation, Conversation)
