from db import teams
from success_rates import filtering


def filter_of_team():
    te = filtering()
    for team in te:
        print(
            f"the {team[0]} team played {team[2]} earned {team[1]} points, and won 0 times: ")


filter_of_team()
