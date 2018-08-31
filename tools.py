import threading
import modules.aircv as aircv
import modules.wda as wda
import modules.aircv as ac
import matplotlib.pyplot as plt
import math
from constants import *
import time


def time_print(content):
    newTime = time.strftime("%H:%M:%S", time.localtime())
    print (newTime + " : " + content)

def analyze_screen():
    time_print ('start analyze screen')
    update_screen()
    plt.imshow(state.screen, cmap = plt.get_cmap())
    pos=plt.ginput(2)
    (h, w) = screen.shape[:2]
    x1 = pos[0][1] * 0.5
    y1 = (SCREEN_WIDTH - pos[0][0]) * 0.5
    x2 = pos[1][1] * 0.5
    y2 = (SCREEN_WIDTH - pos[1][0]) * 0.5
    point1 = [round(x1), round(y1)]
    point2 = [round(x2), round(y2)]
    print ('point 1 : ', end='')
    print (point1)
    print ('point 2 : ', end='')
    print (point2)
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    print ("the distance is ", end='')
    print (distance)
    time_print ('finish analyze screen')

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
    # plt.pause(time)
    gap(time)

def swipe(start, end, gap_time):
    s.swipe(299, start, 299, end, 0.1)
    print("swipe success")
    gap(gap_time)
    update_screen()

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
        return 0
    touch(data, 1)
    print("select success")
    return 1

def select_all(target, confidence):
    data = find_all(target, confidence)
    if (data == None):
        print("can not select the target")
        return 0
    for entity in data:
        touch(entity, 0)
    print("select success")
    return len(data)

def select_list(targets, confidence):
    data = find_list(targets, confidence)
    if (data == None):
        print("can not select the target")
        return 0
    for entity in data:
        touch(entity, 0)
    print("select success")
    return len(data)

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

def weight_anchor():
    touch(WEIGH_ANCHOR, 1)
    update_screen()
    battle_end_confirm = find_one(BATTLE_END_CONFIRM, 0.9)
    while (battle_end_confirm == None):
        update_screen()
        touch(CONTINUE, 0.5)
        battle_end_confirm = find_one(BATTLE_END_CONFIRM, 0.9)
    touch(CONFIRM, 1)

def select_all_ships(targets, try_times):
    update_screen()
    length = len(targets)
    
    while (try_times > 0):
        update_screen()
        length -= select_list(targets, 0.9)
        print(length)
        if (length <= 0):
            print("finish!!!!!!")
            return 0
        swipe(220, 150, 0.5)
        try_times -= 1
    return length

def go_to(target):
    touch(target, 1)
    update_screen()

def screen_click():
    update_screen()
    plt.ion()
    plt.imshow(state.screen)
    pos = plt.ginput(1)
    plt.close()
    plt.ioff()
    x1 = pos[0][1] * 0.5
    y1 = (SCREEN_WIDTH - pos[0][0]) * 0.5
    point1 = [round(x1), round(y1)]
    print ('point 1 is : ', end='')
    print (point1)
    touch(point1, 0)

