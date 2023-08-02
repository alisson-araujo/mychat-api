from ..conversation_repository import ConversationRepository
import pytest


@pytest.mark.skip(reason="Not needed for now")
def test_insert_conversation():
    mocked_name = "talk"

    repository = ConversationRepository()

    r = repository.insert_conversation(mocked_name)
    
    assert r is not None
