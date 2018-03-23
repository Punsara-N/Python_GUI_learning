import os
import io
from currentTime import currentTime
import time

class LogLevel:
    '''Define logging levels.'''
    OFF = 0
    MINIMUM = 1
    NORMAL = 2
    DEBUG = 3
    
class Logger:
    ''' Create a test log and write to it. '''

    def __init__(self, fullTestName, loglevel=LogLevel.DEBUG):
        testName = os.path.splitext(os.path.basename(fullTestName))[0]
        logName = testName + '.log'
        
        logsFolder = 'logs'
        if not os.path.exists(logsFolder):
            os.makedirs(logsFolder)
            
        self.log = os.path.join(logsFolder, logName)
        self.createLog()
        self.loggingLevel = loglevel
        self.startTime = time.clock() #time.perf_counter()

    def createLog(self):
        with io.open(self.log, mode='w', encoding='utf-8') as logFile:
            logFile.write(unicode(currentTime()) + '\t\t*** Starting Test ***\n')
        logFile.close()
        
    def writeToLog(self, msg='', loglevel=LogLevel.DEBUG):
        # control how much gets logged
        if loglevel > self.loggingLevel:
            return
        
        # open log file in append mode
        with io.open(self.log, mode='a', encoding='utf-8') as logFile:
            msg = str(msg)
            if msg.startswith('\n'):
                msg = msg[1:]
            logFile.write(unicode(currentTime())+ '\t\t' + msg + '\n')
        logFile.close()