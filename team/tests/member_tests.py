import pytest
from team.models import Member
from team.tests.fixtures import client, member_data

#positive case
@pytest.mark.django_db
def test_create_member(client: client, member_data: member_data) -> None:    
    for data in member_data:
        response = client.post('/api/member/', data)
        assert response.status_code == 201
        assert response.data['email'] == data['email']
        assert Member.objects.filter(email=data['email']).exists()

@pytest.mark.django_db
def test_get_members(client:client) -> None:
    response = client.get('/api/team/')
    assert response.status_code == 200
    assert len(response.data) == Member.objects.count()

@pytest.mark.django_db
def test_retrieve_member(client: client, member_data: member_data) -> None:

    for data in member_data:
        member = Member.objects.create(first_name=data['first_name'], last_name=data['last_name'], email=data['email'])

        response = client.get(f'/api/member/{member.id}/')
        assert response.status_code == 200
        assert response.data['email'] == data['email']

@pytest.mark.django_db
def test_update_member(client: client, member_data: member_data) -> None:
    member = Member.objects.create(first_name='Jane', last_name='Doe', email='jane@example.com')
    
    for data in member_data:
        response = client.put(f'/api/member/{member.id}/', data)
        assert response.status_code == 200
        assert Member.objects.get(id=member.id).email == data['email']

@pytest.mark.django_db
def test_delete_member(client: client, member_data: member_data) -> None:
    for data in member_data:
        member = Member.objects.create(first_name=data['first_name'], last_name=data['last_name'], email=data['email'])

        response = client.delete(f'/api/member/{member.id}/')
        assert response.status_code == 204
        assert not Member.objects.filter(id=member.id).exists()

#negative case
@pytest.mark.django_db
def test_create_member_missing_required_fields(client: client, member_data: member_data) -> None:
    for data in member_data:
        response = client.post('/api/member/', data={k: data[k] for k in list(data.keys())[:2]})
        assert response.status_code == 400
        assert 'email' in response.data
        assert not Member.objects.exists()

@pytest.mark.django_db
def test_get_nonexistent_member_detail(client: client) -> None:
    response = client.get('/api/team/999/')
    assert response.status_code == 404

@pytest.mark.django_db
def test_update_nonexistent_member(client: client, member_data: member_data) -> None:
    for data in member_data:
        response = client.put('/api/team/999/', data=data)
        assert response.status_code == 404

@pytest.mark.django_db
def test_delete_nonexistent_member(client: client) -> None:
    response = client.delete('/api/team/999/')
    assert response.status_code == 404