from django.urls import path, include
from rest_framework.routers import DefaultRouter

from team.views import MemberViewSet, TeamViewSet

router = DefaultRouter()
router.register(r'team', TeamViewSet)
router.register(r'member', MemberViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
