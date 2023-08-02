from ..settings.connection import DBConnectionHandler
from ..entities.user import User
from src.data.interfaces.user_repository import UserRepositoryInterface


class UserRepository(UserRepositoryInterface):
    @classmethod
    def insert_user(cls, username: str, phone: str, password: str) -> int:
        with DBConnectionHandler() as db_connection:
            try:
                new_user = User(username=username, phone=phone, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()
                return new_user.id
            except Exception as exception:
                db_connection.session.rollback()
                raise exception

    @classmethod
    def get_user_by_phone(cls, phone: str) -> User:
        with DBConnectionHandler() as db_connection:
            try:
                user = db_connection.session.query(User).filter_by(phone=phone).first()
                return user
            except Exception as exception:
                db_connection.session.rollback()
                raise exception
