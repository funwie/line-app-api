from pytest import fixture

from user import User


@fixture
def user() -> User:
    return User(
        id=1, first_name='Jonathan', last_name='Wick', email='johnathanwick@gmail.com', avatar='https://iammg.png'
    )


def test_user_create(user: User):
    assert user