from ..conversation_participants_repository import CvsParticipantsRepository


def test_insert_participant():
    mocked_conversation_id = 1
    mocked_user_id = 1
    repository = CvsParticipantsRepository()
    r = repository.insert_conversation_participant(
        conversation_id=mocked_conversation_id, user_id=mocked_user_id
    )

    assert r != None
