#!/usr/bin/env python

from functools import reduce
import sys

def digital_root(n):
    if len(str(n)) > 1:
        return digital_root(reduce(lambda sum, x: sum + int(x), list(str(n)), 0))
    else:
        return n

if __name__ == '__main__':
    print(digital_root(sys.argv[1]))
