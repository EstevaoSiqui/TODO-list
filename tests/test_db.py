from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from models import User, table_registry


def test_create_user_db():
    engine = create_engine('sqlite:///:memory:')

    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        user = User(
            username='johndoe',
            email='teste@email.com',
            password='123456',
        )
        session.add(user)
        session.commit()
        session.refresh(user)

        result = session.scalar(
            select(User).where(User.email == 'teste@email.com')
        )
    assert result.username == 'johndoe'
