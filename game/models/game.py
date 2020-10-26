# --------------------------------------
#   This file should contain match and player models
# --------------------------------------

from django.db import models
from django.contrib.auth.models import User
from game.models.general import Base

# Base stats of teams
class Teams(Base):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Sessions(Base):
    token = models.CharField(max_length=45)

class UserSessionStats(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey("game.sessions", on_delete=models.CASCADE)
    ranking_position = models.SmallIntegerField(default=0)

# Match Data
class Matchs(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey("game.sessions", on_delete=models.CASCADE)
    team_red = models.ForeignKey("game.teams", related_name="red_team_matchs", on_delete=models.CASCADE)
    team_blue = models.ForeignKey("game.teams", related_name="blue_team_matchs", on_delete=models.CASCADE)
    winner = models.ForeignKey("game.teams", related_name="victories", on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)

# Base stats of individual players
class Players(Base):

    FOOT_SIDE_CHOICES = (
        (0, 'Left'),
        (1, 'Right')
    )

    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=150)
    
    ratings = models.IntegerField(default=0) # 0 to 100? 
    strength = models.IntegerField(default=0)# Agressiviness?
    agility = models.IntegerField(default=0)# Velocity
    resistence = models.IntegerField(default=0)# Duration in game ?

    foot = models.IntegerField(null=False, blank=False, choices=FOOT_SIDE_CHOICES)
    position = models.CharField(max_length=45)
    team = models.ForeignKey("game.teams", related_name="player", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.position}'
    