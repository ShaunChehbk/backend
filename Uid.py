import time
import calendar

def genUid():
    current_GMT = time.gmtime()
    ts = calendar.timegm(current_GMT)
    return ts