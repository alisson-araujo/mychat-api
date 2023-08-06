from ..register_message import RegisterMessage
from src.db.repositories.message_repository import MessageRepository


def test_register_message():
    conversation_id = 1
    user_id = 1
    text = "A message test"

    message_repository = MessageRepository()
    register_message = RegisterMessage(message_repository)

    id = register_message.register(conversation_id, user_id, text)

    assert id is not None
