from django.db import models

# Create your models here.

# choices to player foot
FOOT = (
  ('Left', 'Left'),
  ('Right', 'Right'),
)

class League(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return '{0}'.format(self.name)

class Club(models.Model):
    name = models.CharField(max_length=20)
    rating = models.IntegerField(default=0)
    attack = models.IntegerField(default=0)
    midfield = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)

    def __unicode__(self):
        return '{0}'.format(self.name)

class TeamCoach(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    common_name = models.CharField(max_length=20)
    nation = models.CharField(max_length=20)
    club = models.ForeignKey('Club')
    league = models.ForeignKey('League')

    def __unicode__(self):
        return '{0}'.format(self.common_name)

class Player(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    common_name = models.CharField(max_length=20)
    nation = models.CharField(max_length=20)
    club = models.ForeignKey('Club')
    league = models.ForeignKey('League')
    height = models.FloatField()
    foot = models.CharField(max_length=5, choices=FOOT)

    def __unicode__(self):
        return '{0}'.format(self.common_name)

