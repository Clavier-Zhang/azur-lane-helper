import threading
import lib.aircv as aircv
import lib.wda as wda
import lib.aircv as ac
import matplotlib.pyplot as plt
import math
from constants import *

c = wda.Client(URL)
s = c.session()

# TOOLS

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

def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()

def gap(time):
    e = threading.Event()
    e.wait(time)

def get_screen():
    c.screenshot('screen.png')
    screen = ac.imread('screen.png')
    return screen

def touch(point):
    s.tap(point[0] ,point[1])
    print("touch", end="")
    print(point)
    gap(1)