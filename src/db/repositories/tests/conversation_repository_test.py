from ..conversation_repository import ConversationsRepository
import pytest


@pytest.mark.skip(reason="Not needed for now")
def test_insert_conversation():
    mocked_name = "mocked_name"

    repository = ConversationsRepository()

    r = repository.insert_conversation(mocked_name)

    assert r == None
