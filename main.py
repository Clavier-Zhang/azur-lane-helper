import modules.aircv as aircv
import modules.wda as wda
import modules.aircv as ac

from constants import *
from tools import *
from mission import *
from battle import *
from day import *
from ships import *


HOME_SIDE_BAR =  [9.0, 202.0]
MISSION_COMPLETE = aircv.imread('./image/home/MISSION_COMPLETE.png')
COIN = aircv.imread('./image/home/COIN.png')
GASOLIN = aircv.imread('./image/home/GASOLIN.png')
MISSION_EMPTY = aircv.imread('./image/home/MISSION_EMPTY.png')
HOME_CONTINUE = [133.0, 52.0]

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
    
def collect_one_mission():
    update_screen()
    result = select_one(MISSION_COMPLETE, 0.9)
    if (result == 0):
        return result
    touch(HOME_CONTINUE, 1)
    touch(HOME_CONTINUE, 1)
    touch(HOME_CONTINUE, 1)
    return result
 
def collect_all_missions():
    update_screen()
    result = collect_one_mission()
    while (result == 1):
        result = collect_one_mission()
    print("no mission can be collected")


def collect_resource():
    update_screen()
    result = select_one(COIN, 0.8)
    if (result == 1):
        touch(HOME_CONTINUE, 0.5)
        print("collect coin success")
    update_screen()
    result = select_one(GASOLIN, 0.8)
    update_screen()
    data = find_one(GASOLIN, 0.8)
    if (data != None):
        print("gasolin reach the limit")
        return
    if (result == 1):
        touch(HOME_CONTINUE, 0)

def collect_all():
    print("start collecting all")
    touch(HOME_SIDE_BAR, 1)
    update_screen()
    collect_resource()
    collect_all_missions()


    result = exist(MISSION_EMPTY, 0.9)
    touch(CONTINUE, 0.5)

    if (result):
        do_mission()

#start_game()

# analyze_screen()

update_screen()
# print(find_one(MISSION_DD, 0.9))
# do_day_event()
# collect_all()
# do_mission()
battle_helper()
# print(find_all_enemy())