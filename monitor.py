import threading
import modules.aircv as aircv
import modules.wda as wda
import modules.aircv as ac
import matplotlib.pyplot as plt
import math
from constants import *
from tools import *

def screen_click():
    print("start")
    update_screen()
    plt.ion()
    plt.imshow(state.screen)
    plt.pause(1)
    # pos = plt.ginput(1)
    plt.close()
    plt.ioff()
    # x1 = pos[0][1] * 0.5
    # y1 = (SCREEN_WIDTH - pos[0][0]) * 0.5
    # point1 = [round(x1), round(y1)]
    # print ('point 1 is : ', end='')
    # print (point1)
    # touch(point1, 0)

while (True):
    screen_click()
# plt.imshow(state.screen, cmap = plt.get_cmap())
# screen_click()