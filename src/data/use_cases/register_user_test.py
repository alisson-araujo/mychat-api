# from src.db.repositories.user_repository import UserRepository
from .register_user import RegisterUser
from src.db.tests.user_repository import MockUserRepository

def test_user_register():
    mocked_user_name = "Jonas test"
    mocked_phone = "11999999999"
    mocked_password = "123456789"

    user_repository = MockUserRepository()
    register_user = RegisterUser(user_repository)

    user = register_user.register(mocked_user_name, mocked_phone, mocked_password)
    
    assert user is not None
