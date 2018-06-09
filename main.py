import modules.aircv as aircv
import modules.wda as wda
import modules.aircv as ac

from constants import *
from tools import *
from mission import *
from battle import *
from day import *
from ships import *


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

# analyze_screen()
# swipe(70, 0.2)
# select_all_ships([CLEVELAND, HELENA, HOUSTON, A_UNICORN, A_RAFI])
do_mission()
# update_screen()
# print(count(MISSION_GOING, 0.5))
# select_all_ships([S_BELFAST])
# print(state.mission_fleets)

# print(state.mission_fleets)
