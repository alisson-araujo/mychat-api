from ..message_repository import MessageRepository
import pytest


@pytest.mark.skip(reason="Not needed for now")
def test_insert_message():
    mocked_conversation_id = 1
    mocked_user_id = 1
    mocked_content = "Hello"

    repository = MessageRepository()

    r = repository.insert_message(
        conversation_id=mocked_conversation_id,
        user_id=mocked_user_id,
        content=mocked_content,
    )

    assert r is not None

def test_get_message_by_conversation_id():
    mocked_conversation_id = 1

    repository = MessageRepository()

    r = repository.get_message_by_conversation_id(
        conversation_id=mocked_conversation_id,
    )
    print(r)
    assert r is not None
