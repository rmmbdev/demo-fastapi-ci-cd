import pytest
from utils import create_db


@pytest.fixture(scope="session", autouse=True)
def db_session():
    _ = create_db()
