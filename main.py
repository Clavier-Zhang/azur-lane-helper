import modules.aircv as aircv
import modules.wda as wda
import modules.aircv as ac

from constants import *
from tools import *




def count(target, screen):
    data = ac.find_all_template(screen, target)
    results = []
    for entity in data:
        if (entity['confidence'] > 0.95):
            results.append(entity)
    return len(results)

def swipe_little():
    s.swipe(MISSION_SWIPE_START[0], MISSION_SWIPE_START[1], MISSION_SWIPE_END[0], MISSION_SWIPE_END[1], 0.2)
    print("swipe success")
    gap(3)

# fleet = one or two
def select_fleet(fleet, screen):
    if (fleet == 'one'):
        result = select(FLEET_ONE_RIGHT, screen)
        if (result == FAIL):
            select(FLEET_ONE_LEFT, screen)
    if (fleet == 'two'):
        result = select(FLEET_TWO_RIGHT, screen)
        if (result == FAIL):
            select(FLEET_TWO_LEFT, screen)

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

def find_fleet(fleet_left, fleet_right, screen):
    result_A = (ac.find_template(screen, fleet_right))
    result_B = (ac.find_template(screen, fleet_left))
    if (result_A != None):
        x = result_A['result'][1] * 0.5
        y = (SCREEN_WIDTH - result_A['result'][0]) * 0.5
        return [x, y]
    if (result_B != None):
        x = result_B['result'][1] * 0.5
        y = (SCREEN_WIDTH - result_B['result'][0]) * 0.5
        return [x, y]
    return None

def find_all_enemy(screen):
    hard = find_all(ENEMY_HARD, screen, 0.95)
    medium = find_all(ENEMY_MEDIUM, screen, 0.95)
    boss = find_all(BOSS_FEATURE_A, screen, 0.95)
    return hard + medium + boss

def find_all_surprise(screen):
    data = find_all(SURPRISE, screen, 0.95)
    results = []
    for entity in data:
        x = entity[0]
        y = entity[1] + 30
        temp = [x, y]
        results.append(temp)
    return results

def exist(part, screen):
    result = ac.find_template(screen, part)
    
    if result == None:
        return False
    
    confidence = result['confidence']
    if (confidence > 0.95):
        return True
    else:
        return False
    
def detect_screen(screen):
    if (exist(HOME_FEATURE_A, screen)):
        print("This page is home")
        return "home"
    elif (exist(dock, screen)):
        print("This page is dock")
        return "dock"
    elif (exist(CHAPTER_EIGHT_FEATURE_A, screen)):
        print("This is page is chapter 8")
        return "chapter8"
    elif (exist(CHAPTER_ONE_FEATURE_A, screen)):
        print("This page is chapter 1")
        return "chapter1"
    elif (exist(CHAPTER_SEVEN_FEATURE_A, screen)):
        print("This is home")
        return "This page is Chapter 7"
    elif (exist(BATTLE_FEATURE_A, screen)):
        print("This is page is battle")
        return "battle"
    elif (exist(MAP_FEATURE_A, screen)):
        print("This is page is map")
        return "map"
    elif (exist(PREPARE_FEATURE_A, screen)):
        print("This is page is prepare")
        return "prepare"
    elif (exist(END_FEATURE_A, screen)):
        print("This is page is end")
        return "end"
    else:
        print("This is page is unknown")
        return "unknown"


def attack():
    screen = update_screen()
    touch(EIGHT_THREE, 1)
    touch(GO_NOW_A, 1)
    touch(GO_NOW_B, 1)
    return




def determine_action(current_screen, screen):
    if (current_screen == 'chapter1'):
        touch(ONE_THREE, 1)
        touch(GO_NOW_A, 1)
        touch(GO_NOW_B, 1)
    elif (current_screen == 'map'):
        enemies = find_all_enemy(screen)
        if (enemies == []):
            return
        touch(enemies[0], 1)
    elif (current_screen == 'prepare'):
        touch(WEIGH_ANCHOR, 1)
    elif (current_screen == 'battle'):
        return
    elif (current_screen == 'end'):
        touch(CONFIRM, 1)
    elif (current_screen == 'unknown'):
        touch(CONTINUE, 1)
    return


def start_loop():

    update_screen()
    
    current_screen = detect_screen(screen)
    
    determine_action(current_screen, screen)

def start_game():
    setInterval(start_loop, 1)
    

 
#start_game()

#analyze_screen()


update_screen()
#print (find_list([CLEVELAND, HELENA], screen, 0.95))
#select(MISSION_FEATURE_A, screen)
# team_mission(MISSION_TEAM_FOUR)
#select(MISSION_FEATURE_A, screen)
# select_fleet('one', screen)

# find_list([MISSION_FEATURE_A], screen, 0.8))

select_list([CLEVELAND, HELENA], state.screen, 0.8)