import pytest
from flask.testing import FlaskClient
from src.app import create_app

@pytest.fixture
def client() -> FlaskClient:
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client: FlaskClient) -> None:
    """Test that the home page displays the word 'works'."""
    # Arrange
    response = client.get('/')

    # Act
    data = response.data.decode('utf-8')

    # Assert
    assert response.status_code == 200
    assert 'works' in data
