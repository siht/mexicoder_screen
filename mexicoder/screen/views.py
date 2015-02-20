from .serializers import LeagueSerializer, ClubSerializer, TeamCoachSerializer, PlayerSerializer
from .models import League, Club, TeamCoach, Player
from rest_framework import viewsets
# Create your views here.

class LeagueViewSet(viewsets.ModelViewSet):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer

class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

class TeamCoachViewSet(viewsets.ModelViewSet):
    queryset = TeamCoach.objects.all()
    serializer_class = TeamCoachSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
