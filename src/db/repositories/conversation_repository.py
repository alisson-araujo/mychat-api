from ..settings.connection import DBConnectionHandler
from ..entities.conversation import Conversations


class ConversationsRepository:
    @classmethod
    def insert_conversation(cls, name: str):
        with DBConnectionHandler() as db_connection:
            try:
                new_cvs = Conversations(name=name)
                db_connection.session.add(new_cvs)
                db_connection.session.commit()
            except Exception as exception:
                db_connection.session.rollback()
                raise exception
