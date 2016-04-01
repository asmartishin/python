#!/usr/bin/env python3
import math
import json
from random import randint
from datetime import datetime
from pprint import pprint
import time


def file_json_dump(filename, json_data):
    with open(filename, 'w') as out_file:
        json.dump(json_data, out_file)


def file_json_load(filename):
    with open(filename) as in_file:
        return json.load(in_file)


def time_exec(method):
    def timed(*args, **kwargs):
        time_start = time.time()
        result = method(*args, **kwargs)
        time_end = time.time()
        print('{}: {} s'.format(method.__name__, time_end - time_start))
        return result

    return timed


def create_test():
    json_data = []
    for i in range(1000000):
        a = ['1'] + [str(randint(0, 9)) for x in range(12)]
        s = int(''.join(a))
        json_data.append(s)
    file_json_dump('data.json', json_data)


def time_from_timestamp1(timestamp):
    return datetime.fromtimestamp(timestamp // 1000) if int(math.log10(timestamp) + 1) > 9 else datetime.fromtimestamp(
        timestamp)


def time_from_timestamp2(timestamp):
    return datetime.fromtimestamp(timestamp // 1000) if timestamp > 9999999999 else datetime.fromtimestamp(timestamp)


def time_from_timestamp3(timestamp):
    return datetime.fromtimestamp(int(str(timestamp)[:-3])) if len(str(timestamp)) else datetime.fromtimestamp(
        timestamp)


@time_exec
def time_check1(tests):
    for i in tests:
        time_from_timestamp1(i)


@time_exec
def time_check2(tests):
    for i in tests:
        time_from_timestamp2(i)


@time_exec
def time_check3(tests):
    for i in tests:
        time_from_timestamp3(i)


def main():
    tests = file_json_load('data.json')
    time_check1(tests)
    time_check2(tests)
    time_check3(tests)


if __name__ == '__main__':
    main()
