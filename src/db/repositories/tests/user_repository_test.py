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


def test_get_user_by_phone():
    mocked_phone = "5564992784886"
    repository = UserRepository()
    r = repository.get_user_by_phone(phone=mocked_phone)
    assert r is not None
    assert r.phone == mocked_phone


def test_get_users():
    mocked_phones = ["5564992784856", "64992365478", "64992454545"]
    repository = UserRepository()
    r = repository.get_users(list_of_phones=mocked_phones)

    assert len(r) > 0
    assert r is not None
