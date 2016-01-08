#!/usr/bin/env python

import re
from datetime import datetime
from datetime import timedelta
import time

def timeDecrementDays(ntime, days_to_dec):
    time_dec = ntime - timedelta(days_to_dec)
    return time_dec

def inputGetTime():
    while True:
        try:
            start_input = raw_input('Enter time interval start (Enter for 3 months prior to today): ')
            if start_input == '':
                start_3_months_before = timeDecrementDays(datetime.now(), 90)
                start_day, start_month, start_year = start_3_months_before.day, start_3_months_before.month, start_3_months_before.year
            else:
                start_day, start_month, start_year  = re.search('([0-9]{1,2})[^a-zA-Z0-9]+([0-9]{1,2})[^a-zA-Z0-9]+([0-9]{2,4})', start_input).group(1, 2, 3)
            break
        except Exception:
            print('Format: dd.mm.YYYY')
    while True:
        try:
            end_input = raw_input('Enter time interval stop (Enter for today): ')
            if end_input == '':
                end_day, end_month, end_year = datetime.now().day, datetime.now().month, datetime.now().year
            else:
                end_day, end_month, end_year  = re.search('([0-9]{1,2})[^a-zA-Z0-9]+([0-9]{1,2})[^a-zA-Z0-9]+([0-9]{2,4})', end_input).group(1, 2, 3)
            break
        except Exception:
            print('format: dd.mm.YYYY')
    if len(str(start_day)) < 2:
        start_day = "0" + str(start_day)
    if len(str(start_month)) < 2:
        start_month = "0" + str(start_month)
    if len(str(start_year)) < 4:
        start_year = "20" + str(start_year)
    if len(str(end_day)) < 2:
        end_day = "0" + str(end_day)
    if len(str(end_month)) < 2:
        end_month = "0" + str(end_month)
    if len(str(end_year)) < 4:
        end_year = "20" + str(end_year)
    start_time = "%s-%s-%s" % (start_year, start_month, start_day)
    end_time = "%s-%s-%s" % (end_year, end_month, end_day)
    return (start_time, end_time)

if __name__ == '__main__':
    start_time, end_time = inputGetTime()
    print(start_time, end_time)
