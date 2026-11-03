
from client import all_check


def get_team():

    team_id = (input("enter a id for team :"))
    team_name = input("enter a name for team :")
    return all_check(team_id, team_name)


# print(get_team())


def mune():
    print("======tornament manager======")
    while True:
        pick = int(input("""
1. Add team
2. Show all teams
3. Add match result
4. Show standings
5. Show leading team
6. Show best attacking team
7. Show team success rate
8. Show teams without wins
9. Show tournament summary
10. Check championship potential
0. Exit
Choose an option:

       """))
        if pick == 1:
            return get_team()


print(mune())
