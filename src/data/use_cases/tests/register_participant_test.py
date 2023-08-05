from ..register_participant import RegisterParticipant
from src.db.repositories.conversation_participants_repository import CvsParticipantsRepository

def test_register_participant():
    conversation_id = 1
    user_id = 1

    cvs_participants_repository = CvsParticipantsRepository()
    register_participant = RegisterParticipant(cvs_participants_repository)

    id = register_participant.register(conversation_id, user_id)

    assert id is not None