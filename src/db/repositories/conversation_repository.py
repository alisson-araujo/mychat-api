from src.data.interfaces.conversation_repository import ConversationRepositoryInterface
from ..settings.connection import DBConnectionHandler
from ..entities.conversation import Conversation


class ConversationRepository(ConversationRepositoryInterface):
    @classmethod
    def insert_conversation(cls, name: str) -> int:
        with DBConnectionHandler() as db_connection:
            try:
                new_cvs = Conversation(name=name)
                db_connection.session.add(new_cvs)
                db_connection.session.commit()
                return new_cvs.id
            except Exception as exception:
                db_connection.session.rollback()
                raise exception
