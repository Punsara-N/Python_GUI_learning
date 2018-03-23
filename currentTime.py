from datetime import datetime

def currentTime():
    return str(datetime.now())[:23]