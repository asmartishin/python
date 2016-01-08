#!/usr/bin/env python3

from datetime import datetime
from datetime import timedelta
import time

def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print('%s function took %0.3f s' % (f.__name__, (time2 - time1)))
        return ret
    return wrap

def timeIncrementDays(ntime, days_to_inc):
    time_inc = ntime + timedelta(days_to_inc)
    time_inc_zero = '%s-%s-%s 00:00:00' % (time_inc.year, time_inc.month, time_inc.day)
    timestamp_inc = time_to_timestamp(time_inc_zero)
    return time_inc_zero, timestamp_inc

def timeDecrementDays(ntime, days_to_dec):
    time_dec = ntime - timedelta(days_to_dec)
    return time_dec

def timeConvertFromTimestamp(timestamp):
    if len(str(timestamp)) == 13:
        timestamp = int(str(timestamp)[0:-3])
    ntime = datetime.fromtimestamp(timestamp)
    return ntime

def timeTimestamp(timestamp):
    if len(str(timestamp)) == 13:
        timestamp = int(str(timestamp)[0:-3])
    return timestamp

def timeStringConvertToTime(stime):
    try:
        ntime = datetime.strptime(stime, "%Y-%m-%d %H:%M:%S")
    except Exception:
        ntime = datetime.strptime(stime, "%Y-%m-%d")
    return ntime

# str or datetime.datetime
def timeConvertToTimestamp(ntime):
    if type(ntime) == str:
        try:
            timestamp = int(time.mktime(datetime.strptime(ntime, "%Y-%m-%d %H:%M:%S").timetuple()))
        except Exception:
             timestamp = int(time.mktime(datetime.strptime(ntime, "%Y-%m-%d").timetuple()))
    elif type(ntime) ==  datetime:
        timestamp = int(time.mktime(ntime.timetuple()))
    return timestamp

def timeSecondsToTime(seconds):
    intervals = (
        ('w', 604800),  # 60 * 60 * 24 * 7  weeks
        ('d', 86400),   # 60 * 60 * 24      days
        ('h', 3600),    # 60 * 60           hours
        ('m', 60),      #                   minutes
        ('s', 1),       #                   seconds
    )
    result = []
    if seconds == 0:
        result = ["0s"]
    else:
        for name, count in intervals:
            value = seconds // count
            if value:
                seconds -= value * count
                result.append("{}{}".format(value, name))
    return ' '.join(result)
