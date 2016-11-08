from datetime import datetime, timedelta
import time
from dateutil import parser as date_parser
import re
import os
import json
import hashlib
import argparse


class ConfigLoadError(Exception):
    pass


def date_to_timestamp(date):
    return int(time.mktime(date.timetuple()))


def timestamp_to_date(timestamp):
    return datetime.fromtimestamp(timestamp // 1000) if timestamp > 999999999999 else datetime.fromtimestamp(timestamp)


def string_to_date(date_string):
    return date_parser.parse(date_string)


def pre_day_to_string(delta = 0):
    return str(datetime.now().replace(hour = 0, minute = 0, second = 0) - timedelta(delta)).strftime('%Y-%m-%d')


def string_to_hash(string):
    return hashlib.md5(string.encode('utf8')).hexdigest()


def load_config(filename):
    if os.path.isfile(filename):
        try:
            with open(filename) as conf_file:
                return json.load(conf_file)
        except Exception as e:
            raise ConfigLoadError('Config is not a valid json')
    else:
        raise ConfigLoadError('Wrong config path "{}"'.format(filename))


def ceil_division(dividend, divisor):
    return divisor and (dividend // divisor + bool(dividend % divisor))


def time_exec(method):
    def timed(*args, **kwargs):
        time_start = time.time()
        result = method(*args, **kwargs)
        time_end = time.time()
        print('{}: {} s'.format(method.__name__, time_end - time_start))
        return result
    return timed

def parse_arguments(desc):
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('-s', '--start', type=int, required=False, default=1,
                        help='Start of ctime range in days')
    parser.add_argument('-e', '--end', type=int, required=False, default=0,
                        help='End of ctime range in days')
    return parser.parse_args()
