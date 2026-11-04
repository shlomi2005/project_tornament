from db import teams
ranking = []


def sort_teams():
    ranking = sorted(teams, key=lambda t: (
        int(t["points"]), int(t["goals_for"])-int(t["goals_against"]), (t["name"])), reverse=True)
    return ranking


def tavla(ranking):
    print_array = []
    for team in ranking:
        print_array.append(
            f"name {team["name"]} {team["points"]}, played {team["played"]} wins {team["wins"]} draws{team["draws"]} losses {team["losses"]} point difference {team["goals_for"]-team["goals_against"]}")
    return print_array


def top_team(sorted_teams):
    team = sorted_teams[0]
    team_name = team["name"]
    return team_name
