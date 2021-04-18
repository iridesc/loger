"""[
        # None     0
# Ero      1
# War      2
# Inf      3
# Suc      4
    ]
    """

import time

SHOELEVEL = 4
TIMEMARK = False
COLOR = True
FILEPATH = ""

levelTag = {
    'nocolor': {
        1: 'Ero:',
        2: 'War:',
        3: 'Inf:',
        4: 'Suc:',
    },
    'color': {
        1: '\033[1;31;40mEro:\033[0m',
        2: '\033[1;33;40mWar:\033[0m',
        3: '\033[1;34;40mInf:\033[0m',
        4: '\033[1;32;40mSuc:\033[0m',
    }
}


def loger_setting(show_level: int = 4, time_mark: bool = False, color: bool = True, file_path: str = ""):

    global SHOELEVEL,TIMEMARK,COLOR,FILEPATH

    SHOELEVEL = show_level
    TIMEMARK = time_mark
    COLOR = color
    FILEPATH = file_path

def log(log: str, level: int = 3):
    if level <= SHOELEVEL:
        if TIMEMARK:
            log = time.strftime("%Y-%m-%d %H:%M:%S",
                                time.localtime()) + '>' + log

        if FILEPATH:
            with open(FILEPATH, 'a') as f:
                f.write(levelTag['nocolor'][level]+log+'\n')

        if COLOR:
            log = levelTag['color'][level] + log
        else:
            log = levelTag['nocolor'][level]+log

        print(log)


