from rest_framework import serializers

from team.models import Member, Team

class TeamSerializer(serializers.ModelSerializer):
    """
    Serializer for the «Team» model.
    """

    class Meta:
        model = Team
        fields = ["id", "title", "description", "members"]

class MemberSerializer(serializers.ModelSerializer):
    """
    Serializer for the «Member» model.
    """
    
    class Meta:
        model = Member
        fields = ["id", "first_name", "last_name", "email", "teams"]