from ..settings.connection import DBConnectionHandler
from ..entities.user import Users


class UserRepository:
    @classmethod
    def insert_user(cls, username: str, phone: str, password: str):
        with DBConnectionHandler() as db_connection:
            try:
                new_user = Users(username=username, phone=phone, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()
            except Exception as exception:
                db_connection.session.rollback()
                raise exception

    @classmethod
    def get_user_by_phone(cls, phone: str):
        with DBConnectionHandler() as db_connection:
            try:
                user = db_connection.session.query(Users).filter_by(phone=phone).first()
                return user
            except Exception as exception:
                db_connection.session.rollback()
                raise exception
