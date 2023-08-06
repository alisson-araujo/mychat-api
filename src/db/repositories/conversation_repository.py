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

    @classmethod
    def select_conversation_by_id(cls, id: int) -> Conversation:
        with DBConnectionHandler() as db_connection:
            try:
                conversation = (
                    db_connection.session.query(Conversation).filter_by(id=id).first()
                )
                return conversation
            except Exception as exception:
                raise exception
