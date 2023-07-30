from .connection import DBConnectionHandler
import pytest


@pytest.mark.skip(reason="Sensitive test")
def test_create_engine():
    dbconnection_handler = DBConnectionHandler()

    engine = dbconnection_handler.get_engine()

    assert engine is not None
