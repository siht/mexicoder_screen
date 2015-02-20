from .models import League, Club, TeamCoach, Player
from rest_framework import serializers

class LeagueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = League
        fields = ('name',)

class ClubSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Club
        fields = ('name', 'rating', 'attack', 'midfield', 'defense')

class TeamCoachSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TeamCoach
        fields = ('first_name', 'last_name', 'common_name', 'nation', 'club', 'league')

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ('first_name', 'last_name', 'common_name', 'nation', 'club', 'league', 'height', 'foot')
