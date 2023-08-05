from typing import Dict
from src.domain.use_cases.register_user import RegisterUser as RegisterUserInterface
from ..interfaces.user_repository import UserRepositoryInterface
from src.errors.types import HttpBadRequestError


class RegisterUser(RegisterUserInterface):
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.user_repository = user_repository

    def register(self, username: str, phone: str, password: str) -> Dict:
        self.__validate_username(username)
        self.__validate_phone(phone)
        self.__validate_password(password)

        user = self.user_repository.insert_user(username, phone, password)
        return user

    @classmethod
    def __validate_username(cls, username: str) -> None:
        if username is None:
            raise HttpBadRequestError("Username is required")

        if len(username) > 20:
            raise HttpBadRequestError("Username is too long")

    @classmethod
    def __validate_phone(cls, phone: str) -> None:
        if phone is None:
            raise HttpBadRequestError("Phone is required")

        if len(phone) < 11:
            raise HttpBadRequestError("Invalid phone number")

    @classmethod
    def __validate_password(cls, password: str) -> None:
        if password is None:
            raise HttpBadRequestError("Password is required")

        if len(password) < 8:
            raise HttpBadRequestError("Password is too short")

        if len(password) > 20:
            raise HttpBadRequestError("Password is too long")
