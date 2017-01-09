#!/usr/bin/env python3

import sys
import json

def namelist(names):
    return ', '.join(i['name'] for i in names[:-1]) + ' & {}'.format(names[-1]['name']) if len(names) > 1 else (names[0]['name'] if len(names) == 1 else '')

def main():
    print(namelist(json.loads(sys.argv[1])))

if __name__ == "__main__":
    main()
