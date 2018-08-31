from constants import *
from tools import *
from ships import *






CONFIRM = ac.imread('./image/battle_state/confirm.png')
MAP_START = ac.imread('./image/battle_state/map_start.png')
DETAIL_START = ac.imread('./image/battle_state/detail_start.png')
BATTLE_PROGRESSING = ac.imread('./image/battle_state/battle_progressing.png')
BATTLE_END = ac.imread('./image/battle_state/battle_end.png')


def get_battle_state():

    confidence = 0.8

    if (exist(CONFIRM, confidence)):
        return "confirm"
    
    if (exist(MAP_START, confidence)):
        return "map"

    if (exist(DETAIL_START, confidence)):
        return "detail"

    if (exist(BATTLE_PROGRESSING, 0.95)):
        return "progressing"

    if (exist(BATTLE_END, 0.99)):
        return "end"

    return "unknown"







def find_fleet_one():
    confidence = 0.4
    result = find_one(FLEET_ONE_RIGHT, confidence)
    if (result == None):
        return find_one(FLEET_ONE_LEFT, confidence)
    return result

def find_fleet_two():
    confidence = 0.4
    result = find_one(FLEET_TWO_RIGHT, confidence)
    if (result == None):
        return find_one(FLEET_TWO_LEFT, confidence)
    return result

def select_fleet_one():
    result = find_fleet_one()
    if (result == None):
        print ("can not find fleet one")
        return FAIL
    touch(result, 0.5)
    return result

def select_fleet_two():
    result = find_fleet_two()
    if (result == None):
        print ("can not find fleet two")
        return FAIL
    touch(result, 0.5)
    return result

def select_fleet(fleet):
    confidence = 0.5
    if (fleet == 'one'):
        result = select_one(FLEET_ONE_RIGHT, confidence)
        if (result == FAIL):
            select_one(FLEET_ONE_LEFT, confidence)
    if (fleet == 'two'):
        result = select_one(FLEET_TWO_RIGHT, confidence)
        if (result == FAIL):
            select_one(FLEET_TWO_LEFT, confidence)






ENEMY_CV = ac.imread('./image/enemies/ENEMY_CV.png')
ENEMY_BB = ac.imread('./image/enemies/ENEMY_BB.png')
ENEMY_DD = ac.imread('./image/enemies/ENEMY_DD.png')
ENEMY_BOSS = ac.imread('./image/enemies/ENEMY_BOSS.png')
ENEMY_M = ac.imread('./image/enemies/enemy_m.png')

ENEMIES = [ENEMY_BB, ENEMY_CV, ENEMY_DD, ENEMY_BOSS, ENEMY_M]



def find_all_enemy():
    results = find_list(ENEMIES, 0.6)
    return results

def sekect_one_enemy():
    results = find_all_enemy()
    if (results == None):
        print("no enemy in this screen")
        return FAIL
    touch(results[0], 0.5)
    return SUCCESS





def battle_helper():
    print("start battle helper")
    while(True):
        update_screen()
        if (exist(BATTLE_SCREEN, 0.9)):
            print("at battle home screen, decide which point to go")
            # screen_click()
        elif (exist(BATTLE_START, 0.9)):
            print("auto mode")
            weight_anchor()
        else:
            print("unknown page")
        
            


def start_battle():

    while (True):
        state = get_battle_state()
        print(state)
        gap(1)