#!/usr/bin/env python

import sys
from datetime import datetime
import time

def get_timestamp(time_string):
    return int(time.mktime(datetime.strptime(time_string, '%Y-%m-%d %H:%M:%S').timetuple()))

if __name__ == '__main__':
    time_string = sys.argv[1]
    print get_timestamp(time_string)
