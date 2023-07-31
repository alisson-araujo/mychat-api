from ..settings.connection import DBConnectionHandler
from ..entities.conversation_participants import CvsParticipants


class CvsParticipantsRepository:
    @classmethod
    def insert_conversation_participant(
        self, conversation_id: int, user_id: int
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
