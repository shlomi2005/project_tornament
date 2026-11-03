
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


def get_team():

    team_id = (input("enter a id for team :"))
    team_name = input("enter a name for team :")
