#!/usr/bin/env python

import datetime


def days_diff(date1, date2):
    return abs((datetime.datetime(*(date1)) - datetime.datetime(*(date2))).days)


if __name__ == '__main__':
    print(days_diff((1982, 4, 19), (1982, 4, 22)))

