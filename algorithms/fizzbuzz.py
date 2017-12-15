#!/usr/bin/env python3

from itertools import cycle, zip_longest, count, islice
import time
import sys

def fizzbuzz1(n):
    #start = time.time()
    for i in range(1, n + 1):
        s = ''
        if i % 3 == 0:
            s += 'Fizz'
        if i % 5 == 0:
            s += 'Buzz'
        print(s or i)
    #stop = time.time()
    #print(stop - start)

def fizzbuzz2(n):
    #start = time.time()
    fizzes = cycle([''] * 2 + ['Fizz'])
    buzzes = cycle([''] * 4 + ['Buzz'])
    both = (f + b for f, b in zip_longest(fizzes, buzzes))
    fizzbuzz = (word or n for word, n in zip_longest(both, count(1)))
    for i in islice(fizzbuzz, n):
        print(i)
        #pass
    #stop = time.time()
    #print(stop - start)

if __name__ == '__main__':
    n = (int(sys.argv[1]))
    fizzbuzz1(n)
    #fizzbuzz2(n)
