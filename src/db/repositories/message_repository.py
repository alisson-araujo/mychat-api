from ..settings.connection import DBConnectionHandler
from ..entities.message import Messages
from typing import List


class MessagesRepository:
    @classmethod
    def insert_message(cls, conversation_id: int, user_id: int, content: str) -> int:
        with DBConnectionHandler() as db_connection:
            try:
                new_msg = Messages(
                    conversation_id=conversation_id, user_id=user_id, content=content
                )
                db_connection.session.add(new_msg)
                db_connection.session.commit()
                return new_msg.id
            except Exception as exception:
                db_connection.session.rollback()
                raise exception

    @classmethod
    def get_messages_by_conversation_id(cls, conversation_id: int) -> List:
        with DBConnectionHandler() as db_connection:
            try:
                messages = (
                    db_connection.session.query(Messages)
                    .filter(Messages.conversation_id == conversation_id)
                    .all()
                )
                return messages
            except Exception as exception:
                db_connection.session.rollback()
                raise exception
