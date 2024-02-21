import pytest
from rest_framework.test import APIClient

@pytest.fixture
def member_data():
    data = []
    for i in range(20):
        data.append({
            'first_name': f'John{i}',
            'last_name': f'Doe{i}',
            'email': f'john{i}@example.com'
        })
    return data

@pytest.fixture
def team_data():
    data = []
    for i in range(20):
        data.append({
        "title": f"Test Team{i}",
        "description": f"Test Description{i}"
        })
    return data

@pytest.fixture
def client():
    return APIClient()