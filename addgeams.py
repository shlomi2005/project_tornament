from db import matches


def get_id_homes():
    get_id_home = int(
        input("enter a id from team home that you want update: "))
    return get_id_home


def get_id_aways():
    get_id_away = int(
        input("enter a id from team away that you want update: "))
    return get_id_away


def get_home_goalss():
    get_home_goals = int(input("enter a number home_goals: "))
    return get_home_goals


def get_away_goalss():
    get_away_goals = int(input("enter a number away_goals: "))

    return get_away_goals
