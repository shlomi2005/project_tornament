teams = [{
    "id": 1, "name": "Maccabi", "played": 0,
    "wins": 0, "draws": 0, "losses": 0,
    "goals_for": 0, "goals_against": 0, "points": 0
}]
games = []


def teamm_validation(teams):
    if len(teams) == 0:
        return False
    return True


def add_team(id, name):
    teams.append({
        "id": id, "name": name, "played": 0,
        "wins": 0, "draws": 0, "losses": 0,
        "goals_for": 0, "goals_against": 0, "points": 0
    })
    return f"good {teams}"


def display_all(teams):
    for team in teams:
        if teamm_validation(team) == False:
            print("No teams to display: ")
        print("id =", Display_id(team), ": ",
              "name =", Display_name(team), ": ",
              "played =", Display_played(team), ": ",
              "points =", Display_points(team), ": ")
    return


def Display_id(team):
    ids = team["id"]
    return ids


def Display_name(team):
    names = team["name"]
    return names


def Display_played(team):
    playeds = team["played"]
    return playeds


def Display_points(iteam):
    points = iteam["points"]
    return points
