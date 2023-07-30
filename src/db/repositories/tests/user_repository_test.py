from ..user_repository import UserRepository
import pytest


@pytest.mark.skip(reason="Not needed for now")
def test_insert_user():
    mocked_name = "mocked_name"
    mocked_phone = "5564992784886"
    mocked_password = "123456"
    repository = UserRepository()
    r = repository.insert_user(
        username=mocked_name, phone=mocked_phone, password=mocked_password
    )

    assert r == None
