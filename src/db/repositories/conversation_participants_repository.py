from ..settings.connection import DBConnectionHandler
from ..entities.conversation_participants import CvsParticipants
from src.data.interfaces.conversation_participants_repository import CvsParticipantsRepositoryInterface
from typing import List


class CvsParticipantsRepository(CvsParticipantsRepositoryInterface):
    @classmethod
    def insert_cvs_participant(
        cls, conversation_id: int, user_id: int
    ) -> int:
        with DBConnectionHandler() as db_connection:
            try:
                new_part = CvsParticipants(
                    conversation_id=conversation_id, user_id=user_id
                )
                db_connection.session.add(new_part)
                db_connection.session.commit()
                return new_part.id
            except Exception as exception:
                db_connection.session.rollback()
                raise exception

    @classmethod
    def get_cvs_participants_by_conversation_id(cls, conversation_id: int) -> List[CvsParticipants]:
        with DBConnectionHandler() as db_connection:
            try:
                cvs_participants = (
                    db_connection.session.query(CvsParticipants)
                    .filter_by(conversation_id=conversation_id)
                    .all()
                )
                return cvs_participants
            except Exception as exception:
                db_connection.session.rollback()
                raise exception