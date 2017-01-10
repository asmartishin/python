#!/usr/bin/env python3

import time
import random
import sys

def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print ('%s function took %0.3f ms' % (f.__name__, (time2 - time1) * 1000.0))
        return ret
    return wrap


@timing
def solution1(A):
    num = 0
    for i in range(len(A)):
        for j in range(i, len(A)):
            if (A[i] == 0) and (A[j] == 1):
                num += 1
    return(num)


@timing
def solution2(A):
    zero = []
    one = []
    num = 0
    for i in range(len(A)):
        if A[i] == 0:
            zero.append(i)
        else:
            one.append(i)
    for i in zero:
        for j in one:
            if (i < j):
                num += 1
    return(num)


@timing
def solution3(A):
    num = 0
    oneplus = 0
    for i in range(len(A)):
        if A[i] == 0:
            oneplus += 1
        if oneplus > 0:
            if (A[i] == 1):
                num += oneplus
                if num > 1000000000:
                    return -1
    return num


def main(length):
    A = []
    for i in range(length):
        A.append(random.randint(0, 1))

    print(solution1(A))
    print(solution2(A))
    print(solution3(A))


main(int(sys.argv[1]))
