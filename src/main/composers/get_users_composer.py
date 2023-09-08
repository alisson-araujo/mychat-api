from src.presentation.controllers.get_users_controller import GetUsersController
from src.db.repositories.user_repository import UserRepository
from src.data.use_cases.get_user import GetUser


def get_users_composer():
    repository = UserRepository()
    use_case = GetUser(repository)
    controller = GetUsersController(use_case)

    return controller.handle
