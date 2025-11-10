import pytest
from pydantic import ValidationError
from app.schemas import UserCreate

def test_usercreate_valid():
    u = UserCreate(username="hardik", email="hardik@example.com", password="abcd1234")
    assert u.username == "hardik"

def test_usercreate_invalid_email():
    with pytest.raises(ValidationError):
        UserCreate(username="x", email="not-an-email", password="abcd1234")

def test_usercreate_short_password():
    with pytest.raises(ValidationError):
        UserCreate(username="abc", email="a@b.com", password="short")