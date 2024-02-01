from django.shortcuts import render
from rest_framework import viewsets

from team.models import Member, Team
from team.serializers import MemberSerializer, TeamSerializer

class TeamViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions to the «Team» model.
    """

    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class MemberViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions to the «Member» model.
    """

    queryset = Member.objects.all()
    serializer_class = MemberSerializer