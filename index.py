# -*- coding: utf-8 -*-

import threading
import lib.aircv as aircv
import lib.wda as wda
import lib.aircv as ac
import matplotlib.pyplot as plt
import math
from src import *

# URL = 'http://192.168.1.65:8100' #家里
URL = 'http://192.168.239.149:8100' #公司
c = wda.Client(URL)
s = c.session()

# Device
SCREEN_WIDTH = 750
SUCCESS = 'SUCCESS'
FAIL = 'FAIL'




# TOOLS
def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()

def gap(time):
    e = threading.Event()
    e.wait(time)
        
def analyze_screen():
    c.screenshot('screen.png')
    screen = ac.imread('screen.png')
    plt.imshow(screen, cmap = plt.get_cmap())
    pos=plt.ginput(2)
    (h, w) = screen.shape[:2]
    x1 = pos[0][1] * 0.5
    y1 = (SCREEN_WIDTH - pos[0][0]) * 0.5
    x2 = pos[1][1] * 0.5
    y2 = (SCREEN_WIDTH - pos[1][0]) * 0.5
    point1 = [x1, y1]
    point2 = [x2, y2]
    print (point1)
    print (point2)
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    print (distance)
    
def get_screen():
    c.screenshot('screen.png')
    screen = ac.imread('screen.png')
    return screen

def touch(point):
    s.tap(point[0] ,point[1])
    print("touch", end="")
    print(point)
    gap(1)

def quick_touch(point):
    s.tap(point[0] ,point[1])
    print("touch", end="")
    print(point)

def find_all(target, screen):
    data = ac.find_all_template(screen, target)
    results = []
    for entity in data:
        confidence = entity['confidence']
        if (confidence < 0.5):
            continue
        x = entity['result'][1] * 0.5
        y = (SCREEN_WIDTH - entity['result'][0]) * 0.5
        temp = [x, y, confidence]
        results.append(temp)
    return results

# 选中所有目标
def select_one(target, screen):
    data = find_all(target, screen)
    if (data == []):
        return FAIL
    touch(data[0])
    return SUCCESS

# 选中所有目标
def select(target, screen):
    data = find_all(target, screen)
    for point in data:
        quick_touch(point)
    return

# 选中所有不同种类目标
def select_all(targets, screen):
    for target in targets:
        select(target, screen)

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
        result = select_one(FLEET_ONE_RIGHT, screen)
        if (result == FAIL):
            select_one(FLEET_ONE_LEFT, screen)
    if (fleet == 'two'):
        result = select_one(FLEET_TWO_RIGHT, screen)
        if (result == FAIL):
            select_one(FLEET_TWO_LEFT, screen)
# retire
#def find_target(target, screen):

# 委托
# require: call this function in the chapter screen
def team_mission(team):

    screen = get_screen()
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
        swipe_little()
        screen = get_screen()
        available_mission = count(MISSION_FEATURE_A, screen)
        print("can't find missions in this page, try swipe")
    print(available_mission, end='')
    print(" missions are available")



    if (working_teams == 3):
        print("this is the special mission, need level 100")
        return

    select_one(MISSION_FEATURE_A, screen)

    touch(MISSION_MEMBER_CHOOESE)
    swipe_little()
    print("swipe")
    if (working_teams >= 2):
        swipe_little()
    
    screen = get_screen()
    select_all(team, screen)
    touch(MISSION_CONFIRM)
    touch(MISSION_START)
    touch(CONTINUE)

def check_mission(teams):
    touch(MISSION)
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
    hard = find_all(ENEMY_HARD, screen)
    medium = find_all(ENEMY_MEDIUM, screen)
    boss = find_all(BOSS_FEATURE_A, screen)
    return hard + medium + boss

def find_all_surprise(screen):
    data = find_all(SURPRISE, screen)
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
    screen = get_screen()
    touch(EIGHT_THREE)
    touch(GO_NOW_A)
    touch(GO_NOW_B)
    return




def determine_action(current_screen, screen):
    if (current_screen == 'chapter1'):
        touch(ONE_THREE)
        touch(GO_NOW_A)
        touch(GO_NOW_B)
    elif (current_screen == 'map'):
        enemies = find_all_enemy(screen)
        if (enemies == []):
            return
        touch(enemies[0])
    elif (current_screen == 'prepare'):
        touch(WEIGH_ANCHOR)
    elif (current_screen == 'battle'):
        return
    elif (current_screen == 'end'):
        touch(CONFIRM)
    elif (current_screen == 'unknown'):
        touch(CONTINUE)
    return


def start_loop():

    screen = get_screen()
    
    current_screen = detect_screen(screen)
    
    determine_action(current_screen, screen)
    #print(detect_screen(screen))
    #print (ac.find_all_template(screen, target))
    #s.tap(x ,y)


def start_game():
    setInterval(start_loop, 1)
    

 
#start_game()

#analyze_screen()


screen = get_screen()

#select_one(MISSION_FEATURE_A, screen)
team_mission(MISSION_TEAM_FOUR)

# attack()
# select_fleet('one', screen)