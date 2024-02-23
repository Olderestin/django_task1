import pytest
from rest_framework.test import APIClient

@pytest.fixture
def client() -> None:
    """
    Fixture providing an instance of Django REST Framework's APIClient.
    """
    yield APIClient()