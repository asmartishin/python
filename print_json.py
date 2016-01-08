#!/usr/bin/env python

from __future__ import print_function
import pprint
from datetime import datetime
import time
import json
import sys

def get_filename():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = raw_input('Enter file name: ')
    return filename

def time_timestamp_to_time(timestamp):
    if len(str(timestamp)) == 13:
        timestamp = int(str(timestamp)[0:-3])
    ntime = datetime.fromtimestamp(timestamp)
    return ntime

class JsonPrinter(pprint.PrettyPrinter):
    def format(self, object, context, maxlevels, level):
        if isinstance(object, unicode):
            return (object.encode('utf8'), True, False)
        return pprint.PrettyPrinter.format(self, object, context, maxlevels, level)

def print_json_with_date(json_data, indent = ''):
    for key, value in json_data.iteritems():
        if key == "$date":
            value = ' ' + str(time_timestamp_to_time(value))
        if isinstance(value, list):
            print(key + ':', end = '')
            print()
            indent += '  '
            for list_item in value:
                if isinstance(list_item, dict):
                    print_json_with_date(list_item, indent + '  ')
                else:
                    print(indent + list_item)
        elif isinstance(value, dict):
            print(indent + key + ':', end = '')
            print()
            print_json_with_date(value, indent + '  ')
        else:
            print(indent + key + ':', end = '')
            print(value)

if __name__ == '__main__':
    filename = get_filename()
    with open(filename) as json_file:
        print_json_with_date(json.load(json_file))
