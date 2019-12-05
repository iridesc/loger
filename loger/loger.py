import time
LogerLevel = 4
LogerTimeMark = False
LogerColor = True
LogerOutputFile = None

# None     0
# Ero      1
# War      2
# Inf      3
# Suc      4

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


def setting(logerLevel=4, logerTimeMark=False, logerColor=True, logerOutputFile=None):
    global LogerLevel, LogerColor, LogerOutputFile, LogerTimeMark

    LogerLevel = logerLevel
    LogerTimeMark = logerTimeMark
    LogerColor = logerColor
    LogerOutputFile = logerOutputFile


def makelog(log: str, level: int = 3):
    if level <= LogerLevel:
        if LogerTimeMark:
            log = time.strftime("%Y-%m-%d %H:%M:%S",
                                time.localtime()) + '>' + log
        

        if LogerOutputFile != None:
            with open(LogerOutputFile, 'a') as f:
                f.write(levelTag['nocolor'][level]+log+'\n')

        if LogerColor:
            log = levelTag['color'][level] + log
        else:
            log = levelTag['nocolor'][level]+log

        print(log)

