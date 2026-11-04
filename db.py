teams = [{
    "id": 1, "name": "Maccabi", "played": 0,
    "wins": 0, "draws": 0, "losses": 0,
    "goals_for": 0, "goals_against": 0, "points": 0
}]
games = []


def add_team(id, name):
    teams.append({
        "id": id, "name": name, "played": 0,
        "wins": 0, "draws": 0, "losses": 0,
        "goals_for": 0, "goals_against": 0, "points": 0
    })
    return f"good {teams}"
