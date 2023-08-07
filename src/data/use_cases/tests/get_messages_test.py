from ..get_messages import GetMessages
from src.db.repositories.message_repository import MessageRepository


def test_get_messages():
    mocked_cvs_id = 1
    repository = MessageRepository()
    get_messages = GetMessages(repository)

    messages = get_messages.get_messages(mocked_cvs_id)

    assert messages is not None
    assert len(messages) > 0
