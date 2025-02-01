from models import User


def test_create_user():
    user = User(
        username='johndoe',
        email='teste@email.com',
        password='123456',
    )
    assert user.id is None
