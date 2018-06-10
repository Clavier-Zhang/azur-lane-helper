from constants import *
from tools import *
from ships import *
import json


MISSION = [520, 353] #委托
MISSION_CHOOSE = [185, 165]
MISSION_MEMBER_CHOOESE = [189, 224]
MISSION_CONTINUE = [365.0, 308.0]

MISSION_CONFIRM = [580, 353]

MISSION_START = [548, 232]
MISSION_BACK = [15.0, 12.0]

MISSION_FLEET_ONE = [S_ENTERPRISE, CLEVELAND, HELENA, HOUSTON, FIREFLY, LEXINGTON]
MISSION_FLEET_TWO = [S_BELFAST, YORK, ELIZABETH, FLETCHER, NORFOLK, SANDIEGO]
MISSION_FLEET_THREE = [S_WARSPITE, TIRPITZ, S_YU, S_QUAN, A_UNICORN, ZEPPELIN]
MISSION_FLEET_FOUR = [S_Z46, A_RAFI, B_REPULSE, A_ARIZONA, Z23, A_BIAOQIANG]

MISSION_FLEETS = [MISSION_FLEET_ONE, MISSION_FLEET_TWO, MISSION_FLEET_THREE, MISSION_FLEET_FOUR]

MISSION_GOING = ac.imread('./image/missions/MISSION_GOING.png')
MISSION_FINISHING = ac.imread('./image/missions/MISSION_FINISHING.png')
MISSION_FEATURE = ac.imread('./image/missions/MISSION_FEATURE.png')
MISSION_BOSS = ac.imread('./image/missions/MISSION_BOSS.png')


def choose_fleet(fleet_number):
    if (fleet_number == 1):
        return MISSION_FLEET_ONE
    elif (fleet_number == 2):
        return MISSION_FLEET_TWO
    elif (fleet_number == 3):
        return MISSION_FLEET_THREE
    elif (fleet_number == 4):
        return MISSION_FLEET_FOUR

    
def start_one_mission():
    mission_available = count(MISSION_FEATURE, 0.8)
    if (mission_available == 0):
        print("can't find missions in this page, try swipe")
        swipe(220, 150, 0.5)
        mission_available = count(MISSION_FEATURE, 0.7)
    print(mission_available, end=' ')
    print(" missions are available")
    select_one(MISSION_FEATURE, 0.7)
    touch(MISSION_MEMBER_CHOOESE, 0.5)
    update_screen()

    for fleet in MISSION_FLEETS:
        result = select_all_ships(fleet, 3)
        print("result is ", end='')
        print(result)
        if (result <= 0):
            print("current fleet is ok")
            touch(MISSION_CONFIRM, 0.5)
            touch(MISSION_START, 0.5)
            touch(MISSION_CONTINUE, 0.5)
            break
        print("current is busy, try next")
        touch(MISSION_BACK, 0.5)
        touch(MISSION_MEMBER_CHOOESE, 0.5)
        # print(fleet, end = '')
        


def do_mission():
    print("start do mission")
    go_to(HOME_START)
    go_to(MISSION)

    mission_going = count(MISSION_GOING, 0.5)
    mission_finishing = 4 - count(MISSION_BOSS, 0.7) - (count(MISSION_FEATURE, 0.7)) - count(MISSION_GOING, 0.7)
    print(mission_going, end = ' ')
    print("missions are going")
    if (mission_going == 4):
        print("All missions are set")
        touch(GO_BACK, 0.5)
        return

    while (mission_going < 4):
        start_one_mission()
        mission_going += 1

    touch(MISSION_BACK, 0.5)
    touch(MISSION_BACK, 0.5)
    



    
    


