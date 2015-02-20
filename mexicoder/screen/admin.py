from django.contrib import admin
from .models import League, Club, TeamCoach, Player

# Register your models here.

class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'attack', 'midfield', 'defense')

class TeamCoachAdmin(admin.ModelAdmin):
    list_display = ('common_name', 'first_name', 'last_name', 'nation', 'club', 'league')

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('common_name', 'first_name', 'last_name', 'nation', 'club', 'league', 'height', 'foot')

admin.site.register(League)
admin.site.register(Club, ClubAdmin)
admin.site.register(TeamCoach, TeamCoachAdmin)
admin.site.register(Player, PlayerAdmin)
