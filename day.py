from constants import *
from tools import *
import modules.aircv as ac
from ships import *


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
    touch(ENTER_DAY_EVENT, 0.5)
    touch(CHIP_MODE_MINE, 1)
    weight_anchor()

def get_one_box():
    touch(ENTER_DAY_EVENT, 0.5)
    touch(BOX_MODE, 0.5)
    weight_anchor()

def get_one_book():
    touch(ENTER_DAY_EVENT, 0.5)
    touch(BOOK_MODE, 0.5)
    weight_anchor()

def get_one_gadget():
    touch(ENTER_DAY_EVENT, 0.5)
    touch(GADGET_MODE, 0.5)
    weight_anchor()
    
def get_all_chip():
    get_one_chip()
    get_one_chip()
    get_one_chip()

def get_all_box():
    touch(CHOOSE_DAY_BOX, 0.5)
    get_one_box()
    get_one_box()
    get_one_box()

def get_all_book():
    touch(CHOOSE_DAY_BOOK, 0.5)
    get_one_book()
    get_one_book()
    get_one_book()

def get_all_gadget():
    touch(CHOOSE_DAY_GADGET, 0.5)
    get_one_gadget()
    get_one_gadget()
    get_one_gadget()

def do_day_event():
    print("start day event")
    go_to(HOME_START)
    touch(DAY_EVENT, 0.5)
    day = state.weekday
    # get_all_chip()
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

        # get_all_gadget()
        # touch(GO_BACK, 0.5)
        # touch(MISSION, 0.5)

        get_all_book()
        touch(GO_BACK, 0.5)
        touch(MISSION, 0.5)
        get_all_box()
        touch(GO_BACK, 0.5)
        touch(GO_BACK, 0.5)
        