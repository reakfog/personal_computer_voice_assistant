import sys  
sys.path = ['', '..'] + sys.path[1:]

import datetime
from assistance_bot import settings

def current_datetime():
    if settings.DEBUG == True:
        return datetime.datetime.now()
    return ''
