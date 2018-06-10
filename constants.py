
import time
import modules.aircv as aircv
import modules.wda as wda
import modules.aircv as ac
import json

URL = 'http://192.168.1.65:8100' #家里
# URL = 'http://192.168.239.149:8100' #公司
# URL = 'http://192.168.199.134:8100' #太湖

c = wda.Client(URL)
s = c.session()


class State:
    
    def __init__(self):
        self.screen = None
        self.weekday = time.localtime(time.time()).tm_wday
        self.mission_fleets = [None, True, True, True, True,]


state = State()

file = open('state.json','r',encoding='utf-8')  
fleets_data = json.load(file)  
state.mission_fleets = fleets_data

# Event
C1 = [139, 127]
EVENT_CHAPTER_ONE = ac.imread('./image/event/EVENT_CHAPTER_ONE.png')

# Device
SCREEN_WIDTH = 750
SUCCESS = 'SUCCESS'
FAIL = 'FAIL'



HOME_START = [567.0, 206.0]

dock = aircv.imread('./image/dock.png')  #船坞
SURPRISE = aircv.imread('./image/SURPRISE.png')
BATTLE_FEATURE_A = aircv.imread('./image/BATTLE_FEATURE_A.png')
HOME_FEATURE_A = aircv.imread('./image/HOME_FEATURE_A.png')
MAP_FEATURE_A = aircv.imread('./image/MAP_FEATURE_A.png')
PREPARE_FEATURE_A = aircv.imread('./image/PREPARE_FEATURE_A.png')
END_FEATURE_A = aircv.imread('./image/END_FEATURE_A.png')



# reitire
CLEAN = [256, 260] #退役
SIDE_BAR_START = [647, 135] #退役界面
SIDE_BAR_END = [647, 316]



# General
CHAPTER_SCREEN = ac.imread('./image/CHAPTER_SCREEN.png')
GO_NOW_A = [482, 254]  #第一个立刻前往
GO_NOW_B = [553, 323]  #第一个立刻前往
WEIGH_ANCHOR = [550, 332]  #出击
CONTINUE = [631.0, 184.0] #继续
BATTLE_END_CONFIRM = ac.imread('./image/BATTLE_END_CONFIRM.png')
CONFIRM = [570, 320] #确认
GO_BACK = [17.0, 14.0]

ESCAPE = [474, 196]
AMBUSH = ac.imread('./image/AMBUSH.png')

PREVIOUS_CHAPTER = [31, 189] #前一章
NEXT_CHAPTER = [637, 189] #下一章
SIMULATION = [617, 353] #演习

# Chapter 8
CHAPTER_EIGHT_FEATURE_A = ac.imread('./image/chapters/CHAPTER_EIGHT_FEATURE_A.png')
EIGHT_ONE = [288, 99]
EIGHT_TWO = [144, 188]
EIGHT_THREE = [176, 297]


# Chapter 7
CHAPTER_SEVEN_FEATURE_A = ac.imread('./image/chapters/CHAPTER_SEVEN_FEATURE_A.png')

# Chapter 1
CHAPTER_ONE_FEATURE_A = ac.imread('./image/chapters/CHAPTER_ONE_FEATURE_A.png')
ONE_ONE = [80, 237]
ONE_TWO = [238, 143]
ONE_THREE = [344, 275]
ONE_FOUR = [415, 93]

# Chapter 1
TWO_ONE = [426, 239]
TWO_TWO = [392, 97]
TWO_THREE = [146, 143]
TWO_FOUR = [204, 285]

# Ships
FLEET_ONE_LEFT = ac.imread('./image/ships/FLEET_ONE_LEFT.png')
FLEET_ONE_RIGHT = ac.imread('./image/ships/FLEET_ONE_RIGHT.png')
FLEET_TWO_RIGHT = ac.imread('./image/ships/FLEET_TWO_RIGHT.png')
FLEET_TWO_LEFT = ac.imread('./image/ships/FLEET_TWO_LEFT.png')

ENEMY_HARD = ac.imread('./image/ships/ENEMY_HARD.png')
ENEMY_MEDIUM = ac.imread('./image/ships/ENEMY_MEDIUM.png')
BOSS_FEATURE_A = ac.imread('./image/ships/BOSS_FEATURE_A.png')


ENEMY_CV = ac.imread('./image/enemies/ENEMY_CV.png')
ENEMY_BB = ac.imread('./image/enemies/ENEMY_BB.png')
ENEMY_DD = ac.imread('./image/enemies/ENEMY_DD.png')
ENEMY_BOSS = ac.imread('./image/enemies/ENEMY_BOSS.png')

ENEMIES = [ENEMY_BB, ENEMY_CV, ENEMY_DD, ENEMY_BOSS]

