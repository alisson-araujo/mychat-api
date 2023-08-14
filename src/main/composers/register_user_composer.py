from src.db.repositories.user_repository import UserRepository
from src.data.use_cases.register_user import RegisterUser
from src.presentation.controllers.register_user_controller import RegisterUserController


def register_user_composer():
    repository = UserRepository()
    use_case = RegisterUser(repository)
    controller = RegisterUserController(use_case)

    return controller.handle
