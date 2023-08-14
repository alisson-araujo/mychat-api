from src.db.repositories.user_repository import UserRepository
from src.data.use_cases.get_user import GetUser
from src.presentation.controllers.get_user_controller import GetUserController


def get_user_composer():
    repository = UserRepository()
    use_case = GetUser(repository)
    controller = GetUserController(use_case)

    return controller.handle
