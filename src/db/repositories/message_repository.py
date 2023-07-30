from ..settings.connection import DBConnectionHandler
from ..entities.message import Messages


class MessagesRepository:
    def insert_message(cls, conversation_id: int, user_id: int, content: str):
        with DBConnectionHandler() as db_connection:
            try:
                new_msg = Messages(
                    conversation_id=conversation_id, user_id=user_id, content=content
                )
                db_connection.session.add(new_msg)
                db_connection.session.commit()
            except Exception as exception:
                db_connection.session.rollback()
                raise exception
