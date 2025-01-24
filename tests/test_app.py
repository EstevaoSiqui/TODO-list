from http import HTTPStatus

from fastapi.testclient import TestClient

from todo_fastapi.app import app


def test_read_root_return_OK():
    client = TestClient(app)  # Arrange (organização)
    response = client.get('/')  # Act (ação)
    assert response.status_code == HTTPStatus.OK  # Assert (verificação)
    assert response.json() == {'message': 'Ola mundo'}
