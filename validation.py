from db import teams, add_team


def all_check(id, name):
    num_validations = number_check(id)
    name_validations = name_check(name)
    if num_validations == "ok" and name_validations == "ok":
        result = add_team(id, name)
        return result
    if num_validations != "ok":
        return num_validations
    if name_validations != "ok":
        return name_validations


def number_check(numbers):
    if not id_not_duplicate(numbers):
        return "please enter another number: "
    if not id_validation(numbers):
        return "please enter a valid numbers: "
    return "ok"


def name_check(name):
    if not name_validation(name):
        return "please enter a valid name: "
    if not name_not_duplicate(name):
        return "name is uplicate enter a name new: "
    return "ok"


def name_validation(name) -> str:
    if not (name.strip()):
        return None
    return True


def id_validation(numbers):
    try:
        int(numbers)
    except ValueError:
        return None
    return int(numbers) > 0


def id_not_duplicate(numbers) -> int:
    for team in teams:
        if team["id"] == numbers:
            return None
    return True


def name_not_duplicate(name) -> str:
    for team in teams:
        if team["name"].upper() == name.upper:
            return None
    return True
