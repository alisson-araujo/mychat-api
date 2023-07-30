from ..conversation_repository import ConversationsRepository


def test_insert_conversation():
    mocked_name = "mocked_name"

    repository = ConversationsRepository()

    r = repository.insert_conversation(mocked_name)

    assert r == None
