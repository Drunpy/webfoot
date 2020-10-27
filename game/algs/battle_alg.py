from typing import NewType

Team = NewType('Team', int)

class TeamBattle(object):

    def compute_result(self, team_one: Team, team_two: Team):
        print("Team one", team_one)
        print("Team two", team_two)

        team_one_players = team_one.players.all()
        team_two_players = team_two.players.all()

        team_one_stats = []
        for player_to in team_one_players:
            team_one_stats.append([player_to.strength, player_to.resistence])

        team_two_stats = []
        for player_tt in team_two_players:
            team_two_stats.append([player_tt.strength, player_tt.resistence])

        team_one_score = 0
        team_two_score = 0

        teams_stats = team_one_stats + team_two_stats
        for index, stat in enumerate(teams_stats):
            try:
                if stat[0] < teams_stats[index+1][0]:
                    team_one_score+=1
                else:
                    team_two_score+=1
            except:
                pass

        print(f"Stats {team_one_stats} - {team_two_stats}")
        winner = team_one if team_one_score > team_two_score else team_two
        return f"Battle {team_one}({team_one_stats}) x {team_two}({team_two_stats}) -> {winner}"