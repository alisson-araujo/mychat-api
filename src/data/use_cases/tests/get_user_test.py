from src.db.repositories.user_repository import UserRepository
from ..get_user import GetUser
from src.db.entities.user import User


def test_find_user():
    mocked_user_phone = "5564992784886"
    user_repository = UserRepository()
    get_user = GetUser(user_repository)

    user = get_user.get_user_by_phone(mocked_user_phone)
    assert user is not None
    assert isinstance(user, User)
