#!/usr/bin/env python

import sys
from datetime import datetime

def get_datetime(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    timestamp = int(sys.argv[1])
    print get_datetime(timestamp)

