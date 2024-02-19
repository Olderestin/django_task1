import pytest
from rest_framework.test import APIClient
from team.models import Team

#positive case
@pytest.mark.django_db
def test_create_team():
    client = APIClient()
    data = {
        "title": "Test Team",
        "description": "Test Description"
        }
    response = client.post('/api/team/', data=data)
    assert response.status_code == 201
    assert response.data['title'] == "Test Team"
    assert Team.objects.filter(title="Test Team").exists()

@pytest.mark.django_db
def test_get_teams():
    client = APIClient()
    response = client.get('/api/team/')
    assert response.status_code == 200
    assert len(response.data) == Team.objects.count()

@pytest.mark.django_db
def test_retrieve_team():
    team = Team.objects.create(title="Test Team", description="Test Description")
    client = APIClient()
    response = client.get(f'/api/team/{team.id}/')
    assert response.status_code == 200
    assert response.data['title'] == "Test Team"

@pytest.mark.django_db
def test_update_team():
    team = Team.objects.create(title="Test Team", description="Test Description")
    
    client = APIClient()
    
    data = {
        "title": "Updated Team",
        "description": "Updated Description"
        }
    
    response = client.put(f'/api/team/{team.id}/', data=data)
    assert response.status_code == 200
    assert Team.objects.get(id=team.id).title == "Updated Team"

@pytest.mark.django_db
def test_delete_team():   
    team = Team.objects.create(title="Test Team", description="Test Description")
    
    client = APIClient()
    
    response = client.delete(f'/api/team/{team.id}/')
    assert response.status_code == 204
    assert not Team.objects.filter(id=team.id).exists()

#negative case
@pytest.mark.django_db
def test_create_team_missing_required_fields():
    client = APIClient()
    
    data = {
        "description": "Test Description"
        }
    
    response = client.post('/api/team/', data=data)
    assert response.status_code == 400
    assert 'title' in response.data
    assert not Team.objects.exists()

@pytest.mark.django_db
def test_get_nonexistent_team_detail():
    client = APIClient()
    
    response = client.get('/api/team/999/')
    assert response.status_code == 404

@pytest.mark.django_db
def test_update_nonexistent_team():
    client = APIClient()
    
    data = {
        "title": "Updated Team",
        "description": "Updated Description"
        }
    
    response = client.put('/api/team/999/', data=data)
    assert response.status_code == 404

@pytest.mark.django_db
def test_delete_nonexistent_team():
    client = APIClient()
    
    response = client.delete('/api/team/999/')
    assert response.status_code == 404
