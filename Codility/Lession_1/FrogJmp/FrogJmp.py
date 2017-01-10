#!/usr/bin/env python

import sys

def solution(x, y, d):
    count = 0
    while x < y:
        count += 1
        x += d
    print count

if __name__ == '__main__':
    solution(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
