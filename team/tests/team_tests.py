from dataclasses import asdict

import pytest

from team.models import Team
from team.tests.conftest import client
from team.tests.test_data import create_team_data
from team.tests.schemas import TeamData

#positive case
@pytest.mark.parametrize("data", create_team_data())
@pytest.mark.django_db
def test_create_team(client: client, data: TeamData) -> None:
    """
    Test creating a team via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
        data: Team data.
    """
    response = client.post('/api/team/', data=asdict(data))
    assert response.status_code == 201
    assert response.data["title"] == data.title
    assert Team.objects.filter(title=data.title).exists()

@pytest.mark.django_db
def test_get_teams(client:client) -> None:
    """
    Test retrieving list of teams via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
    """
    response = client.get('/api/team/')
    assert response.status_code == 200
    assert len(response.data) == Team.objects.count()

@pytest.mark.parametrize("data", create_team_data())
@pytest.mark.django_db
def test_retrieve_team(client: client, data: TeamData) -> None:
    """
    Test retrieving a specific team via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
        data: Team data.
    """
    team = Team.objects.create(title=data.title, description=data.description)

    response = client.get(f'/api/team/{team.id}/')
    assert response.status_code == 200
    assert response.data["title"] == data.title

@pytest.mark.parametrize("data", create_team_data())
@pytest.mark.django_db
def test_update_team(client: client, data: TeamData) -> None:
    """
    Test updating a team via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
        data: Team data.
    """
    team = Team.objects.create(title="Test Team", description="Test Description")
    
    response = client.put(f'/api/team/{team.id}/', data=asdict(data))
    assert response.status_code == 200
    assert Team.objects.get(id=team.id).title == data.title

@pytest.mark.parametrize("data", create_team_data())
@pytest.mark.django_db
def test_delete_team(client: client, data: TeamData) -> None:
    """
    Test deleting a team via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
        data: Team data.
    """
    team = Team.objects.create(title=data.title, description=data.description)

    response = client.delete(f'/api/team/{team.id}/')
    assert response.status_code == 204
    assert not Team.objects.filter(id=team.id).exists()

#negative case
@pytest.mark.parametrize("data", create_team_data())
@pytest.mark.django_db
def test_create_team_missing_required_fields(client: client, data: TeamData) -> None:
    """
    Test creating a team with missing required fields via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
        data: Team data.
    """
    response = client.post('/api/team/', data={key: value for key, value in data.__dict__.items() if key in ['description']})
    assert response.status_code == 400
    assert 'title' in response.data
    assert not Team.objects.exists()

@pytest.mark.django_db
def test_get_nonexistent_team_detail(client: client) -> None:
    """
    Test retrieving details of a nonexistent team via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
    """
    response = client.get('/api/team/999/')
    assert response.status_code == 404

@pytest.mark.parametrize("data", create_team_data())
@pytest.mark.django_db
def test_update_nonexistent_team(client: client, data: TeamData) -> None:
    """
    Test updating a nonexistent team via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
        data: Team data.
    """
    response = client.put('/api/team/999/', data=asdict(data))
    assert response.status_code == 404

@pytest.mark.django_db
def test_delete_nonexistent_team(client: client) -> None:
    """
    Test deleting a nonexistent team via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
    """    
    response = client.delete('/api/team/999/')
    assert response.status_code == 404
