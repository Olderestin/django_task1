import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from team.models import Member

#positive case
@pytest.mark.django_db
def test_create_member():
    client = APIClient()
    
    data = {
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john@example.com'
    }
    
    response = client.post('/api/member/', data)
    assert response.status_code == 201
    assert response.data['email'] == "john@example.com"
    assert Member.objects.filter(email="john@example.com").exists()

@pytest.mark.django_db
def test_get_members():
    client = APIClient()
    
    response = client.get('/api/team/')
    assert response.status_code == 200
    assert len(response.data) == Member.objects.count()

@pytest.mark.django_db
def test_retrieve_member():
    member = Member.objects.create(first_name='Jane', last_name='Doe', email='jane@example.com')

    client = APIClient()
    
    response = client.get(f'/api/member/{member.id}/')
    assert response.status_code == 200
    assert response.data['email'] == "jane@example.com"

@pytest.mark.django_db
def test_update_member():
    member = Member.objects.create(first_name='Jane', last_name='Doe', email='jane@example.com')
    
    client = APIClient()
    
    data = {
        'first_name': 'Updated',
        'last_name': 'Updated',
        'email': 'jane_updated@example.com'
    }
    
    response = client.put(f'/api/member/{member.id}/', data)
    assert response.status_code == 200
    assert Member.objects.get(id=member.id).email == "jane_updated@example.com"

@pytest.mark.django_db
def test_delete_member():
    member = Member.objects.create(first_name='Jane', last_name='Doe', email='jane@example.com')

    client = APIClient()

    response = client.delete(f'/api/member/{member.id}/')
    assert response.status_code == 204
    assert not Member.objects.filter(id=member.id).exists()

#negative case
@pytest.mark.django_db
def test_create_member_missing_required_fields():
    client = APIClient()
    
    data = {
        'first_name': 'John',
        'last_name': 'Updated'
        }
    
    response = client.post('/api/member/', data=data)
    assert response.status_code == 400
    assert 'email' in response.data
    assert not Member.objects.exists()

@pytest.mark.django_db
def test_get_nonexistent_member_detail():
    client = APIClient()
    
    response = client.get('/api/team/999/')
    assert response.status_code == 404

@pytest.mark.django_db
def test_update_nonexistent_member():
    client = APIClient()
    
    data = {
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john@example.com'
        }
    
    response = client.put('/api/team/999/', data=data)
    assert response.status_code == 404

@pytest.mark.django_db
def test_delete_nonexistent_member():
    client = APIClient()
    
    response = client.delete('/api/team/999/')
    assert response.status_code == 404