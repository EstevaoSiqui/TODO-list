import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import table_registry
from todo_fastapi.app import app


@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')
    table_registry.metadata.create_all(engine)


    table_registry.metadata.drop_all(engine)
