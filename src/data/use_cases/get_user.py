from typing import List
from src.domain.use_cases.get_user import GetUser as GetUserInterface
from src.data.interfaces.user_repository import UserRepositoryInterface
from src.errors.types import HttpNotFoundError, HttpBadRequestError
from src.db.entities.user import User


class GetUser(GetUserInterface):
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.user_repository = user_repository

    def get_user_by_phone(self, phone: str) -> User:
        self.__validate_phone(phone)
        user = self.user_repository.get_user_by_phone(phone)
        if user is None:
            raise HttpNotFoundError("User not found")
        return user

    @classmethod
    def __validate_phone(cls, phone: str) -> None:
        if phone is None:
            raise HttpBadRequestError("Phone number is required")

        if len(phone) > 20:
            raise HttpBadRequestError("Phone number is too long")

    def get_users(self, list_of_phones: list) -> List:
        for phone in list_of_phones:
            self.__validate_phone(phone)

        users = self.user_repository.get_users(list_of_phones)
        if users is None:
            raise HttpNotFoundError("Users not found")
        return users
