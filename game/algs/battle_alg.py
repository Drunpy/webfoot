from typing import NewType
from random import randint
Team = NewType('Team', int)

class TeamBattle(object):

    def compute_result(self, team_one: Team, team_two: Team):
        print("Team one", team_one)
        print("Team two", team_two)

        team_one_power = team_one.power + randint(0, 7)
        team_two_power = team_two.power + randint(0, 7)

        print("Power: ", team_one.power, team_two.power)
        print("Luck Fac: ", team_one_power, team_two_power)
        winner = team_one if team_one_power > team_two_power else team_two
        
        return f"{winner} is the winner of battle between {team_one} and {team_two}"