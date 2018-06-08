import threading
import modules.aircv as aircv
import modules.wda as wda
import modules.aircv as ac
import matplotlib.pyplot as plt
import math
from constants import *

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

def update_screen():
    c.screenshot('screen.png')
    screen = ac.imread('screen.png')
    return screen

def touch(point, time):
    s.tap(point[0] ,point[1])
    print("touch", end="")
    print(point)
    gap(time)

def find_one(target, screen, target_confidence):
    data = ac.find_template(screen, target)
    if (data == None):
        return None
    confidence = data['confidence']
    if (confidence < target_confidence):
        return None
    x = data['result'][1] * 0.5
    y = (SCREEN_WIDTH - data['result'][0]) * 0.5
    return [x, y, confidence]

def find_all(target, screen, target_confidence):
    data = ac.find_all_template(screen, target)
    results = []
    for entity in data:
        confidence = entity['confidence']
        if (confidence < target_confidence):
            continue
        x = entity['result'][1] * 0.5
        y = (SCREEN_WIDTH - entity['result'][0]) * 0.5
        temp = [x, y, confidence]
        results.append(temp)
    if (results == []):
        return None      
    return results

def find_list(targets, screen, target_confidence):
    results = []
    for target in targets:
        temp = find_all(target, screen, target_confidence)
        if (temp == None):
            continue
        results += temp
    if (results == []):
        return None
    return results

def select_one(target, screen, confidence):
    data = find_one(target, screen, confidence)
    if (data == None):
        print("cannot select target")
        return FAIL
    touch(data[0], 1)
    return SUCCESS