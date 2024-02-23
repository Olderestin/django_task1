from dataclasses import asdict

import pytest

from team.models import Member
from team.tests.conftest import client
from team.tests.test_data import create_member_data
from team.tests.schemas import MemberData

#positive case
@pytest.mark.parametrize("data", create_member_data())
@pytest.mark.django_db
def test_create_member(client: client, data: MemberData) -> None:
    """
    Test creating a member via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
        data: Member data.
    """   
    data = asdict(data)

    response = client.post('/api/member/', data)
    assert response.status_code == 201
    assert response.data['email'] == data['email']
    assert Member.objects.filter(email=data['email']).exists()

@pytest.mark.django_db
def test_get_members(client:client) -> None:
    """
    Test retrieving list of members via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
    """
    response = client.get('/api/team/')
    assert response.status_code == 200
    assert len(response.data) == Member.objects.count()

@pytest.mark.parametrize("data", create_member_data())
@pytest.mark.django_db
def test_retrieve_member(client: client, data: MemberData) -> None:
    """
    Test retrieving a specific member via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
        data: Member data.
    """
    data = asdict(data)

    member = Member.objects.create(first_name=data['first_name'], last_name=data['last_name'], email=data['email'])

    response = client.get(f'/api/member/{member.id}/')
    assert response.status_code == 200
    assert response.data['email'] == data['email']

@pytest.mark.parametrize("data", create_member_data())
@pytest.mark.django_db
def test_update_member(client: client, data: MemberData) -> None:
    """
    Test updating a member via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
        data: Member data.
    """
    data = asdict(data)

    member = Member.objects.create(first_name='Jane', last_name='Doe', email='jane@example.com')

    response = client.put(f'/api/member/{member.id}/', data)
    assert response.status_code == 200
    assert Member.objects.get(id=member.id).email == data['email']

@pytest.mark.parametrize("data", create_member_data())
@pytest.mark.django_db
def test_delete_member(client: client, data: MemberData) -> None:
    """
    Test deleting a member via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
        data: Member data.
    """
    data = asdict(data)

    member = Member.objects.create(first_name=data['first_name'], last_name=data['last_name'], email=data['email'])

    response = client.delete(f'/api/member/{member.id}/')
    assert response.status_code == 204
    assert not Member.objects.filter(id=member.id).exists()

#negative case
@pytest.mark.parametrize("data", create_member_data())
@pytest.mark.django_db
def test_create_member_missing_required_fields(client: client, data: MemberData) -> None:
    """
    Test creating a member with missing required fields via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
        data: Member data.
    """
    data = asdict(data)

    response = client.post('/api/member/', data={k: data[k] for k in list(data.keys())[:2]})
    assert response.status_code == 400
    assert 'email' in response.data
    assert not Member.objects.exists()

@pytest.mark.django_db
def test_get_nonexistent_member_detail(client: client) -> None:
    """
    Test retrieving details of a nonexistent member via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
    """
    response = client.get('/api/team/999/')
    assert response.status_code == 404

@pytest.mark.parametrize("data", create_member_data())
@pytest.mark.django_db
def test_update_nonexistent_member(client: client, data: MemberData) -> None:
    """
    Test updating a nonexistent member via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
        data: Member data.
    """
    data = asdict(data)

    response = client.put('/api/team/999/', data=data)
    assert response.status_code == 404

@pytest.mark.django_db
def test_delete_nonexistent_member(client: client) -> None:
    """
    Test deleting a nonexistent member via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
    """
    response = client.delete('/api/team/999/')
    assert response.status_code == 404