from ..settings.connection import DBConnectionHandler
from ..entities.user import User
from src.data.interfaces.user_repository import UserRepositoryInterface
from typing import List
from sqlmodel import select


class UserResult:
    def __init__(self, username: str, phone: str) -> None:
        self.username: str = username
        self.phone: str = phone


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

    @classmethod
    def get_users(cls, list_of_phones: list) -> List[UserResult]:
        with DBConnectionHandler() as db_connection:
            try:
                query = select(User).where(User.phone.in_(list_of_phones))
                users = db_connection.session.exec(query)

                users_list = []

                for row in users:
                    user_result = UserResult(row.username, row.phone)
                    users_list.append(user_result)

                return users_list
            except Exception as exception:
                db_connection.session.rollback()
                raise exception
