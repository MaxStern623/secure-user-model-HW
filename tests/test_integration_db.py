import os
import tempfile
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db import Base
from app import models, crud, schemas


def setup_temp_db():
    fd, path = tempfile.mkstemp(suffix='.db')
    os.close(fd)
    url = f"sqlite:///{path}"
    engine = create_engine(url, connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    return Session, path


def teardown_temp_db(path):
    try:
        os.remove(path)
    except OSError:
        pass


def test_create_user_and_uniqueness():
    Session, path = setup_temp_db()
    db = Session()
    try:
        user_in = schemas.UserCreate(username="tester", email="t@example.com", password="pw12345")
        user = crud.create_user(db, user_in)
        assert user.id is not None

        # duplicate username
        user2 = schemas.UserCreate(username="tester", email="other@example.com", password="pw12345")
        try:
            crud.create_user(db, user2)
            assert False, "Expected IntegrityError"
        except Exception:
            pass

        # duplicate email
        user3 = schemas.UserCreate(username="tester2", email="t@example.com", password="pw12345")
        try:
            crud.create_user(db, user3)
            assert False, "Expected IntegrityError"
        except Exception:
            pass
    finally:
        db.close()
        teardown_temp_db(path)
