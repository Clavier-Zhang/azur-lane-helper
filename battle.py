from constants import *
from tools import *
from ships import *


BATTLE_SCREEN = ac.imread('./image/battle/BATTLE_SCREEN.png')
BATTLE_START = ac.imread('./image/battle/BATTLE_START.png')


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

def attack_one():
    print("start attack one")
    update_screen()
    enemies = find_all_enemy()
    while (enemies == None):
        update_screen()
        enemies = find_all_enemy()

    update_screen()
    fleet_one_position = find_fleet_one()
    

    for enemy in enemies:
        touch(enemy, 1)
        position = find_fleet_one()
        if (position[0] == fleet_one_position[0] and position[1] == fleet_one_position[1]):
            continue
        else:
            break
    gap(2)
    if_ambush()
    weight_anchor()

def attack_all():
    print("start attack all")
    update_screen()
    chapter = find_one(CHAPTER_SCREEN, 0.9)
    print(chapter)
    while (chapter == None):
        attack_one()
        update_screen()
        chapter = find_one(CHAPTER_SCREEN, 0.9)
        print(chapter)

def if_ambush():
    update_screen()
    result = find_one(AMBUSH, 0.9)
    if (result == None):
        return
    print("ambushed, try escape")
    touch(ESCAPE, 1)

def start_battle(target):
    touch(target, 0.5)
    touch(GO_NOW_A, 0.5)
    touch(GO_NOW_B, 1)
    attack_all()

def wait_until_show(target):
    while (True):
        if (exist(target, 0.7)):
            return
        else:
            gap(1)

def battle_helper():
    print("start battle helper")
    while(True):
        update_screen()
        if (exist(BATTLE_SCREEN, 0.9)):
            print("at battle home screen, decide which point to go")
            screen_click()
            wait_until_show(BATTLE_START)
        elif (exist(BATTLE_START, 0.9)):
            print("auto mode")
            weight_anchor()
        else:
            print("unknown page")
        
            
