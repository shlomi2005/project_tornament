from db import matches, teams


def add_game(id_h, id_a, goalss_h, goalss_a):
    matches.append({"home_team_id": id_h, "away_team_id": id_a,
                    "home_goals": goalss_h, "away_goals": goalss_a})
    update_temas(id_h, id_a, goalss_h, goalss_a)
    winner(goalss_h, goalss_a)
    # teams.append({})
    return f"good{matches[-1]}"


def update_temas(id_h, id_a, goalss_h, goalss_a):
    for team in teams:
        if team["id"] == id_h:
            team["played"] += 1
            team["goals_for"] += goalss_h
            team["goals_against"] += goalss_a

        if team["id"] == id_a:
            team["played"] += 1
            team["goals_for"] += goalss_a
            team["goals_against"] += goalss_h
        if winner(goalss_h, goalss_a) == goalss_h:
            if team["id"] == id_h:
                team["wins"] += 1
                team["points"] += 3
            elif team["id"] == id_a:
                team["losses"] += 1
        if winner(goalss_h, goalss_a) == goalss_a:
            if team["id"] == id_a:
                team["wins"] += 1
                team["points"] += 3
            elif team["id"] == id_h:
                team["losses"] += 1
        if draws(goalss_h, goalss_a) == "draws":
            if team["id"] == id_a:
                team["points"] += 1
            if team["id"] == id_h:
                team["points"] += 1


def draws(goalss_h, goalss_a):
    if goalss_h == goalss_a:
        return "draws"


def winner(goalss_h, goalss_a):
    if goalss_h > goalss_a:
        return goalss_h
    return goalss_a


def total_validation(id_h, id_a, goalss_h, goalss_a):
    if validation_game_id_goals(id_h, id_a, goalss_h, goalss_a) == True and validation_team_game(id_h, id_a) == True:
        print(add_game(id_h, id_a, goalss_h, goalss_a))


def input_():
    id_h = get_id_homes()
    id_a = get_id_aways()
    goalss_h = get_home_goalss()
    goalss_a = get_away_goalss()
    total_validation(id_h, id_a, goalss_h, goalss_a)


def validation_game_id_goals(id_h, id_a, goalss_h, goalss_a):
    for team in teams:
        if id_h != team["id"] and (id_a != team["id"]):
            print("id not team :")
            return False
        if id_h == id_a:
            print("id home and id away must be different: ")
            return False
        if type(goalss_h) != int or type(goalss_a) != int:
            print("number of goals must be numbr int: ")
            return False
    return True


def validation_team_game(id_h, id_a):
    for game in matches:
        if game["home_team_id"] == id_h or game["home_team_id"] == id_a and game["away_team_id"] == id_h or ["away_team_id"] == id_a:
            print("a team cannot play against the same team twice: ")
            return False
    return True


def get_id_homes():
    get_id_home = int(
        input("enter a id from team home that you want update: "))
    return (get_id_home)


def get_id_aways():
    get_id_away = int(
        input("enter a id from team away that you want update: "))
    return (get_id_away)


def get_home_goalss():
    get_home_goals = int(input("enter a number home goals: "))
    return (get_home_goals)


def get_away_goalss():
    get_away_goals = int(input("enter a number away goals: "))

    return (get_away_goals)
