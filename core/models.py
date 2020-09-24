from django.db import models
from django.contrib.auth.models import User

class Base(models.Model):
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

# User data
class Data(Base):
    pass

# Base stats of teams
class Teams(Base):
    name = models.CharField(max_length=150)

class Sessions(Base):
    token = models.CharField(max_length=45)

class UserSessionStats(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey("core.sessions", on_delete=models.CASCADE)
    ranking_position = models.SmallIntegerField(default=0)

# Match Data
class Matchs(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey("core.sessions", on_delete=models.CASCADE)
    team_red = models.ForeignKey("core.teams", related_name="red_team_matchs", on_delete=models.CASCADE)
    team_blue = models.ForeignKey("core.teams", related_name="blue_team_matchs", on_delete=models.CASCADE)
    winner = models.ForeignKey("core.teams", related_name="victories", on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)

# Base stats of individual players
class Players(Base):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=150)
    
    ratings = models.IntegerField(default=0) # 0 to 100? 
    strength = models.IntegerField(default=0)# Agressiviness?
    agility = models.IntegerField(default=0)# Velocity
    resistence = models.IntegerField(default=0)# Duration in game ?

    foot = models.CharField(max_length=10)# left or right?
    position = models.CharField(max_length=4)# GK(GL), DF(ZG), ...?
    
