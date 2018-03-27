from datetime import datetime

def currentTime():
    return str(datetime.now())[:23]

def currentTimeText():
    a = str(datetime.now())[:23]
    c = _addUnderscore('-', a)
    c = _addUnderscore(' ', c)
    c = _addUnderscore(':', c)
    c = _addUnderscore('.', c)
    return c

def _addUnderscore(replaceThis, x):
    b = x.split(replaceThis)
    c = ''
    for i in range(len(b)):
        c = c + '_' + b[i]
    return c[1:]
    
if __name__ == '__main__':
    print(currentTimeText())