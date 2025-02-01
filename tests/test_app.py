from http import HTTPStatus


def test_read_root_return_OK(client):
    response = client.get('/')  # Act (ação)
    assert response.status_code == HTTPStatus.OK  # Assert (verificação)
    assert response.json() == {'message': 'Ola mundo'}


def test_create_user_return_201(client):
    user_data = {
        'username': 'johndoe',
        'email': 'teste@gmail.com',
        'password': 'sdfgsdfgwer',
    }
    response = client.post('/users/', json=user_data)
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'johndoe',
        'email': 'teste@gmail.com',
    }


def test_read_users_return_list(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'johndoe',
                'email': 'teste@gmail.com',
            }
        ],
    }


def update_user_return_200(client):
    user_data = {
        'password': 'sdfgsdfgwer',
        'username': 'johndoe',
        'email': 'teste@gmail.com',
        'id': 1,
    }

    response = client.put('/users/1', json=user_data)
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'johndoe',
        'email': 'teste@gmail.com',
    }


def teste_delete_user(client):
    response = client.delete('/users/1')
    assert response.json() == {
        'id': 1,
        'username': 'johndoe',
        'email': 'teste@gmail.com',
    }


def test_update_notFound_user(client):
    response = client.put(
        '/users/0',
        json={
            'username': 'johndoe',
            'email': 'teste@gmail.com',
            'password': 'abcd',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_notFound_user(client):
    response = client.delete('/users/0')
    assert response.status_code == HTTPStatus.NOT_FOUND
