import lib.aircv as ac
import lib.aircv as aircv


# Event
C1 = [139, 127]
EVENT_CHAPTER_ONE = ac.imread('./image/event/EVENT_CHAPTER_ONE.png')


# 舰娘
CLEVELAND = ac.imread('./image/ships/standard/CLEVELAND.png')
HELENA = ac.imread('./image/ships/standard/HELENA.png')
FIREFLY = ac.imread('./image/ships/standard/FIREFLY.png')
HOUSTON = ac.imread('./image/ships/standard/HOUSTON.png')
LEXINGTON = ac.imread('./image/ships/standard/LEXINGTON.png')
YORK = ac.imread('./image/ships/standard/YORK.png')

ELIZABETH = ac.imread('./image/ships/standard/ELIZABETH.png')
FLETCHER = ac.imread('./image/ships/standard/FLETCHER.png')
NORFOLK = ac.imread('./image/ships/standard/NORFOLK.png')
SANDIEGO = ac.imread('./image/ships/standard/SANDIEGO.png')
TIRPITZ = ac.imread('./image/ships/standard/TIRPITZ.png')
ZEPPELIN = ac.imread('./image/ships/standard/ZEPPELIN.png')

DOWNS = ac.imread('./image/ships/standard/DOWNS.png')
EDINBURGH = ac.imread('./image/ships/standard/EDINBURGH.png')
SARATOGA = ac.imread('./image/ships/standard/SARATOGA.png')
YORKTON = ac.imread('./image/ships/standard/YORKTON.png')
Z23 = ac.imread('./image/ships/standard/Z23.png')
HORNET = ac.imread('./image/ships/standard/HORNET.png')

A_RAFI = ac.imread('./image/ships/standard/A_RAFI.png')
S_QUAN = ac.imread('./image/ships/standard/S_QUAN.png')
S_YU = ac.imread('./image/ships/standard/S_YU.png')
A_BIAOQIANG = ac.imread('./image/ships/standard/A_BIAOQIANG.png')
A_UNICORN = ac.imread('./image/ships/standard/A_UNICORN.png')
A_INDIANAPOLIS = ac.imread('./image/ships/standard/A_INDIANAPOLIS.png')



# 委托
MISSION_CHOOSE = [185, 165]
MISSION_MEMBER_CHOOESE = [189, 224]


MISSION_SWIPE_START = [299, 286]
MISSION_SWIPE_END = [299, 210]

MISSION_CONFIRM = [580, 353]

MISSION_START = [548, 232]

MISSION_TEAM_ONE = [CLEVELAND, HELENA, HOUSTON, FIREFLY, YORK, LEXINGTON]
MISSION_TEAM_TWO = [ELIZABETH, FLETCHER, NORFOLK, SANDIEGO, TIRPITZ, ZEPPELIN]
MISSION_TEAM_THREE = [HORNET, DOWNS, EDINBURGH, SARATOGA, YORKTON, Z23]
MISSION_TEAM_FOUR = [S_QUAN, S_YU, A_BIAOQIANG, A_INDIANAPOLIS, A_RAFI, A_INDIANAPOLIS]

MISSION_TEAMS = [MISSION_TEAM_ONE, MISSION_TEAM_TWO, MISSION_TEAM_THREE, MISSION_TEAM_FOUR]

WORKING = ac.imread('./image/WORKING.png')
MISSION_FEATURE_A = ac.imread('./image/MISSION_FEATURE_A.png')
MISSION_FEATURE_B = ac.imread('./image/MISSION_FEATURE_B.png')
MISSION_BOSS_FEATURE_A = ac.imread('./image/MISSION_BOSS_FEATURE_A.png')

MISSION_FINISHING_FEATURE_A = ac.imread('./image/MISSION_FINISHING_FEATURE_A.png')


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
GO_NOW_A = [482, 254]  #第一个立刻前往
GO_NOW_B = [553, 323]  #第一个立刻前往
WEIGH_ANCHOR = [550, 332]  #出击
CONTINUE = [325, 302] #继续
CONFIRM = [570, 320] #确认


PREVIOUS_CHAPTER = [31, 189] #前一章
NEXT_CHAPTER = [637, 189] #下一章
EVENT = [413, 351] #每日
MISSION = [520, 353] #委托
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

# Ships
FLEET_ONE_LEFT = ac.imread('./image/ships/FLEET_ONE_LEFT.png')
FLEET_ONE_RIGHT = ac.imread('./image/ships/FLEET_ONE_RIGHT.png')
FLEET_TWO_RIGHT = ac.imread('./image/ships/FLEET_TWO_RIGHT.png')
FLEET_TWO_LEFT = ac.imread('./image/ships/FLEET_TWO_LEFT.png')

ENEMY_HARD = ac.imread('./image/ships/ENEMY_HARD.png')
ENEMY_MEDIUM = ac.imread('./image/ships/ENEMY_MEDIUM.png')
BOSS_FEATURE_A = ac.imread('./image/ships/BOSS_FEATURE_A.png')