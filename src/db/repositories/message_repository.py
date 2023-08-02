from ..settings.connection import DBConnectionHandler
from ..entities.message import Message
from src.data.interfaces.message_repository import MessageRepositoryInterface
from typing import List


class MessageRepository(MessageRepositoryInterface):
    @classmethod
    def insert_message(cls, conversation_id: int, user_id: int, content: str) -> int:
        with DBConnectionHandler() as db_connection:
            try:
                new_msg = Message(
                    conversation_id=conversation_id, user_id=user_id, content=content
                )
                db_connection.session.add(new_msg)
                db_connection.session.commit()
                return new_msg.id
            except Exception as exception:
                db_connection.session.rollback()
                raise exception

    @classmethod
    def get_message_by_conversation_id(cls, conversation_id: int) -> List[Message]:
        with DBConnectionHandler() as db_connection:
            try:
                message = (
                    db_connection.session.query(Message)
                    .filter(Message.conversation_id == conversation_id)
                    .all()
                )
                return message
            except Exception as exception:
                db_connection.session.rollback()
                raise exception
