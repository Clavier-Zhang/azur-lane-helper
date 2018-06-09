import threading
import modules.aircv as aircv
import modules.wda as wda
import modules.aircv as ac
import matplotlib.pyplot as plt
import math
from constants import *


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
    point1 = [round(x1), round(y1)]
    point2 = [round(x2), round(y2)]
    print ('point 1 is : ', end='')
    print (point1)
    print ('point 2 is : ', end='')
    print (point2)
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    print ("the distance is ", "end")
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
    global screen
    screen = ac.imread('screen.png')
    state.screen = screen
    return screen

def touch(point, time):
    s.tap(point[0] ,point[1])
    print("touch", end="")
    print(point)
    gap(time)

def swipe(length, time):
    MISSION_SWIPE_START = [299, 286]
    MISSION_SWIPE_END = [299, 210]
    s.swipe(299, 286, 299, 286 - length, time)
    print("swipe success")
    gap(2)

def find_one(target, target_confidence):
    data = ac.find_template(state.screen, target)
    if (data == None):
        return None
    confidence = data['confidence']
    if (confidence < target_confidence):
        return None
    x = data['result'][1] * 0.5
    y = (SCREEN_WIDTH - data['result'][0]) * 0.5
    return [x, y, confidence]

def find_all(target, target_confidence):
    data = ac.find_all_template(state.screen, target)
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

def find_list(targets, target_confidence):
    results = []
    for target in targets:
        temp = find_all(target, target_confidence)
        if (temp == None):
            continue
        results += temp
    if (results == []):
        return None
    return results

def select_one(target, confidence):
    data = find_one(target, confidence)
    if (data == None):
        print("can not select the target")
        return FAIL
    touch(data, 1)
    print("select success")
    return SUCCESS

def select_all(target, confidence):
    data = find_all(target, confidence)
    if (data == None):
        print("can not select the target")
        return FAIL
    for entity in data:
        touch(entity, 0)
    print("select success")
    return SUCCESS

def select_list(targets, confidence):
    data = find_list(targets, confidence)
    if (data == None):
        print("can not select the target")
        return FAIL
    for entity in data:
        touch(entity, 0)
    print("select success")
    return SUCCESS

def count(target, confidence):
    data = find_all(target, confidence)
    if (data == None):
        return 0
    return len(data)

def count_list(targets, confidence):
    data = find_list(targets, confidence)
    if (data == None):
        return 0
    return len(data)

def exist(target, target_confidence):
    result = ac.find_template(state.screen, target)
    if result == None:
        return False
    confidence = result['confidence']
    if (confidence > target_confidence):
        return True
    else:
        return False