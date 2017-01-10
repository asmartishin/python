#!/usr/bin/env python3

import sys
import subprocess

def solution(X, A):
    s = set()
    for i in range(len(A)):
        s.add(A[i])
        if len(s) == X:
            return i

    return -1

if __name__ == '__main__':
    r = solution(5, [1, 3, 1, 4, 2, 3, 5, 4])
    print (r)
