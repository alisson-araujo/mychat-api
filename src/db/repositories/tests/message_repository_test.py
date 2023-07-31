from ..message_repository import MessagesRepository
import pytest


@pytest.mark.skip(reason="Not needed for now")
def test_insert_message():
    mocked_conversation_id = 1
    mocked_user_id = 1
    mocked_content = "Hello"

    repository = MessagesRepository()

    r = repository.insert_message(
        conversation_id=mocked_conversation_id,
        user_id=mocked_user_id,
        content=mocked_content,
    )

    assert r is not None
