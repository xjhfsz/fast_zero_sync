from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá, mundo!'}  # Assert


def test_html_deve_retornar_ok_e_html_ola_mundo(client):
    response = client.get('/html')

    html = """
    <html>
        <head>
            <title>Olá Mundo!</title>
        </head>
        <body>
        </body>
            <h1>Olá Mundo!</h1>
    </html>
    """

    assert response.status_code == HTTPStatus.OK
    assert response.text == html


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'testuser',
            'password': 'password',
            'email': 'user@test.com',
        },
    )
    assert response.status_code == HTTPStatus.CREATED  # test status code
    assert response.json() == {
        'id': 1,
        'username': 'testuser',
        'email': 'user@test.com',
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'testuser',
                'email': 'user@test.com',
            },
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1/',
        json={
            'id': 1,
            'password': '123',
            'username': 'testuser2',
            'email': 'user@test.com',
        },
    )

    assert response.json() == {
        'id': 1,
        'username': 'testuser2',
        'email': 'user@test.com',
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted!'}
