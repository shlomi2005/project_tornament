
teams = [{
    "id": 1, "name": "Maccabi", "played": 5,
    "wins": 0, "draws": 0, "losses": 0,
    "goals_for": 17, "goals_against": 5, "points": 156
}, {"id": 2, "name": "dana", "played": 4,
    "wins": 0, "draws": 0, "losses": 0,
    "goals_for": 17, "goals_against": 1, "points": 1554
    }]
matches = [{"home_team_id": 14, "away_team_id": 14,
            "home_goals": 14, "away_goals": 14}]


def add_team(id, name):
    teams.append({
        "id": id, "name": name, "played": 0,
        "wins": 0, "draws": 0, "losses": 0,
        "goals_for": 0, "goals_against": 0, "points": 0
    })
    return f"good {teams}"
