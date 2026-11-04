from validation import all_check
# from db import teams
from display import display_all
from add_geams import input_
from rating import tavla, sort_teams, ranking, top_team
from goools_top import top_goals
from success_rates import success
from team_losses import filter_of_team


def get_team():
    team_id = int(input("enter a id for team :"))
    team_name = input("enter a name for team :")
    return all_check(team_id, team_name)


def menu():
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
            print(get_team())
        if pick == 2:
            display_all()
        if pick == 3:
            input_()
        if pick == 4:
            print(tavla(sort_teams()))
        if pick == 5:
            print(top_team(sort_teams()))
        if pick == 6:
            top_goals()
        if pick == 7:
            success()
        if pick == 8:
            filter_of_team()
        if pick == 9:
            pass
        if pick == 10:
            pass
        if pick == 0:
            print("good bye")
            break


menu()
