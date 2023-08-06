from ..get_participants import GetParticipants
from src.db.repositories.conversation_participants_repository import (
    CvsParticipantsRepository,
)


def test_get_participants():
    cvs_id = 1

    repository = CvsParticipantsRepository()
    use_case = GetParticipants(repository)

    participants = use_case.get_participants(cvs_id)

    assert participants is not None
    assert len(participants) > 0
