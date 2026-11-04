from db import teams


def group_sorting(teams):
    team_play = []
    for team in teams:
        if team["played"] > 0:
            team_play.append(team)
    return team_play


def top_goals():
    team_play = group_sorting(teams)
    if len(team_play) == 0:
        print("no teams have played yet: ")
        return
    best = max(team_play, key=lambda t: int(t["goals_for"]))
    highest = best["goals_for"]
    for team in team_play:
        if team["goals_for"] == highest:
            print(f"{team["name"]}, goals_for {team["goals_for"]}")
