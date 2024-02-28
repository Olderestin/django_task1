from dataclasses import dataclass

from pydantic import EmailStr

@dataclass
class MemberData:
    """
    Represents a member with first name, last name, and email.
    """
    first_name: str
    last_name: str
    email: EmailStr

@dataclass
class TeamData:
    """
    Represents a team with title and description.
    """
    title: str
    description: str