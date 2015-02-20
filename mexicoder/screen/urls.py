from django.conf.urls import url, include
from .views import LeagueViewSet, ClubViewSet, TeamCoachViewSet, PlayerViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'leagues', LeagueViewSet)
router.register(r'clubs', ClubViewSet)
router.register(r'coaches', TeamCoachViewSet)
router.register(r'players', PlayerViewSet)

urlpatterns = [
    url(r'^$', include(router.urls)),
    url(r'^api-auth/$', include('rest_framework.urls', namespace='rest_framework'))
]
