from ..conversation_participants_repository import CvsParticipantsRepository
import pytest


@pytest.mark.skip(reason="Not needed for now")
def test_insert_participant():
    mocked_conversation_id = 1
    mocked_user_id = 2
    repository = CvsParticipantsRepository()
    r = repository.insert_cvs_participant(
        conversation_id=mocked_conversation_id, user_id=mocked_user_id
    )

    assert r != None


def test_get_cvsparticipants():
    mocked_conversation_id = 1
    repository = CvsParticipantsRepository()
    r = repository.get_cvs_participants_by_conversation_id(
        conversation_id=mocked_conversation_id
    )
    print(r)
    assert r != None
