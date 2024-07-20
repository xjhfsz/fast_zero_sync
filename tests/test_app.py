from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange (organização)

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
