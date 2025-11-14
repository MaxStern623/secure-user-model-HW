from app.security import hash_password, verify_password


def test_hash_and_verify():
    pw = "secret123"
    h = hash_password(pw)
    assert h != pw
    assert verify_password(pw, h)
    assert not verify_password("wrong", h)
