from typing import List
from team.tests.schemas import MemberData, TeamData

def create_member_data() -> List[MemberData]:
    """
    Create a list of data for members.
    """
    data = []
    for i in range(20):
        data.append(MemberData(
            first_name=f'John{i}',
            last_name=f'Doe{i}',
            email=f'john{i}@example.com'
        ))

    return data

def create_team_data() -> List[TeamData]:
    """
    Create a list of data for teams.
    """
    data = []
    for i in range(20):
        data.append(TeamData(
            title=f"Test Team{i}",
            description=f"Test Description{i}"
        ))
    return data