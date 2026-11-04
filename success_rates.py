from db import teams


def filtering():
    filteri = []
    for team in teams:
        filteri.append((team["name"], team["points"],
                       team["played"], team["wins"]))
    return filteri


def success():
    sumi = filtering()
    total_for_team = 0
    for team in sumi:
        po = team[1]
        pl = team[2]
        if pl == 0:
            print("no games ")
        else:
            total_for_team = po/(pl*3)*100
            print(f"{team[0]} is {total_for_team} %")
