#!/usr/bin/env python3

import sys
import math

def solution(A):
    print (A)
    B = []
    l = len(A)
    A = list(map(int, A))
    for p in range(1, l + 1):
        inc = 0
        dec = 0
        for i in range(p):
            inc += A[i]
        for j in range(p, l):
            dec += A[j]
        count = abs(inc - dec)
        B.append(count)
        #print (str(p) + ' '+ str(inc) + ' ' + str(dec) + ' ' + str(count))
    print (min(B))

if __name__ == '__main__':
    A = sys.argv[1].split(', ')
    solution(A)
