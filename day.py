from constants import *
from tools import *
import modules.aircv as ac
from ships import *

EVENT_LIST  = ac.imread('./image/event/EVENT_LIST.png')

# 每日活动
DAY_EVENT = [413, 351] # 每日 chapter界面中

ENTER_DAY_EVENT = [333.0, 270.0] # 通用进入

CHOOSE_DAY_BOOK = [193.0, 255.0]
CHOOSE_DAY_CHIP = [333.0, 270.0]
CHOOSE_DAY_BOX = [488.0, 273.0]
CHOOSE_DAY_GADGET = [85.0, 252.0]

# 战术研修
CHIP_MODE_MINE = [338.0, 252.0]
CHIP_MODE_FIRE = [336.0, 180.0]
CHIP_MODE_FLY = [306.0, 108.0]

# 斩首行动
BOX_MODE = [256.0, 272.0]

# 海域突进
BOOK_MODE = [256.0, 272.0]

# 商船护送
GADGET_MODE = [256.0, 272.0]


def get_one_chip():
    touch(CHIP_MODE_MINE, 1)
    update_screen()
    if (exist(EVENT_LIST, 0.7)):
        return 0
    weight_anchor()
    return 1

def get_all_chip():
    touch(ENTER_DAY_EVENT, 0.5)
    result = get_one_chip()
    while (result == 1):
        result = get_one_chip()
    touch(GO_BACK, 0.5)
    touch(GO_BACK, 0.5)
    touch(DAY_EVENT, 0.5)
    print("all chips have been collected")

def get_one_box():
    touch(BOX_MODE, 0.5)
    update_screen()
    if (exist(EVENT_LIST, 0.7)):
        return 0
    weight_anchor()
    return 1

def get_one_book():
    touch(BOOK_MODE, 0.5)
    update_screen()
    if (exist(EVENT_LIST, 0.7)):
        return 0
    weight_anchor()
    return 1

def get_one_gadget():
    touch(GADGET_MODE, 0.5)
    update_screen()
    if (exist(EVENT_LIST, 0.7)):
        return 0
    weight_anchor()
    return 1
    
    

def get_all_box():
    touch(CHOOSE_DAY_BOX, 0.5)
    touch(ENTER_DAY_EVENT, 0.5)
    result = get_one_box()
    while (result == 1):
        result = get_one_box()
    touch(GO_BACK, 0.5)
    touch(GO_BACK, 0.5)
    touch(DAY_EVENT, 0.5)
    print("all boxes have been collected")

def get_all_book():
    touch(CHOOSE_DAY_BOOK, 0.5)
    touch(ENTER_DAY_EVENT, 0.5)
    result = get_one_book()
    while (result == 1):
        result = get_one_book()
    touch(GO_BACK, 0.5)
    touch(GO_BACK, 0.5)
    touch(DAY_EVENT, 0.5)
    print("all books have been collected")

def get_all_gadget():
    touch(CHOOSE_DAY_GADGET, 0.5)
    touch(ENTER_DAY_EVENT, 0.5)
    result = get_one_gadget()
    while (result == 1):
        result = get_one_gadget()
    touch(GO_BACK, 0.5)
    touch(GO_BACK, 0.5)
    touch(DAY_EVENT, 0.5)
    print("all gadgets have been collected")

def do_day_event():
    print("start day event")
    go_to(HOME_START)
    touch(DAY_EVENT, 0.5)
    day = state.weekday
    get_all_chip()
    if (day == 0):
        get_all_gadget()
    elif (day == 1):
        get_all_book()
    elif (day == 2):
        get_all_box()
    elif (day == 3):
        get_all_gadget()
    elif (day == 4):
        get_all_book()
    elif (day == 5):
        get_all_box()
    elif (day == 6):
        get_all_gadget()
        get_all_book()
        get_all_box()
    touch(GO_BACK, 0.5)
    touch(GO_BACK, 0.5)
        