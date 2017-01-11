#!/usr/bin/env python

import sys

BASE = {v: i for i,v in (enumerate('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'))}

def checkio(str_number, radix):
    power = len(str_number) - 1
    radix = int(radix)
    result = 0
    for number in str_number:
        if BASE[number] < radix:
            result += BASE[number] * (radix ** power)
            power -= 1
        else:
            return -1
    return result

if __name__ == '__main__':
    print(checkio(sys.argv[1], sys.argv[2]))
