import modules.aircv as aircv
import modules.wda as wda
import modules.aircv as ac

from constants import *
from tools import *
from mission import *
from battle import *
from day import *


# 委托
# require: call this function in the chapter screen
def team_mission(team):

    screen = update_screen()
    working_teams = count(WORKING, screen)
    finishing_teams = 4 - count(MISSION_BOSS_FEATURE_A, screen) - (count(MISSION_FEATURE_B, screen)) - count(WORKING, screen)
    print(working_teams, end = ' ')
    print("teams are working")

    if (finishing_teams > 0):
        print(finishing_teams, end = ' ')
        print(" need to be collected")

    if (working_teams == 4):
        print("Everyone is working")
        return
    
    print("We need more teams")



    available_mission = count(MISSION_FEATURE_A, screen)
    if (available_mission == 0):
        swipe(70, 0.2)
        screen = update_screen()
        available_mission = count(MISSION_FEATURE_A, screen)
        print("can't find missions in this page, try swipe")
    print(available_mission, end='')
    print(" missions are available")



    if (working_teams == 3):
        print("this is the special mission, need level 100")
        return

    select(MISSION_FEATURE_A, screen)

    touch(MISSION_MEMBER_CHOOESE, 1)
    swipe(70, 0.2)
    print("swipe")
    if (working_teams >= 2):
        swipe(70, 0.2)
    
    screen = update_screen()
    select_list(team, screen)
    touch(MISSION_CONFIRM, 1)
    touch(MISSION_START, 1)
    touch(CONTINUE, 1)


def check_mission(teams):
    touch(MISSION, 1)
    for team in teams:
        team_mission(team)




def find_all_surprise(screen):
    data = find_all(SURPRISE, screen, 0.95)
    results = []
    for entity in data:
        x = entity[0]
        y = entity[1] + 30
        temp = [x, y]
        results.append(temp)
    return results




def start_loop():

    update_screen()
    
    current_screen = detect_screen(screen)


def start_game():
    setInterval(start_loop, 1)
    

 
#start_game()

analyze_screen()


# update_screen()
# team_mission(MISSION_TEAM_FOUR)
# print(find_all_enemy())
# start_battle(TWO_ONE)
# attack_all()

# select_one(WEEK_BOOK, 0.7)