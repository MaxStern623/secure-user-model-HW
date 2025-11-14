from app.schemas import UserCreate, UserRead
import pytest
from pydantic import ValidationError


def test_usercreate_valid():
    u = UserCreate(username="alice", email="alice@example.com", password="password")
    assert u.username == "alice"


def test_usercreate_invalid_email():
    with pytest.raises(ValidationError):
        UserCreate(username="bob", email="not-an-email", password="password")


def test_userread_orm_mode():
    data = {"id": 1, "username": "a", "email": "a@example.com", "created_at": None}
    ur = UserRead.from_orm(type("X", (), data)())
    assert ur.email == "a@example.com"
