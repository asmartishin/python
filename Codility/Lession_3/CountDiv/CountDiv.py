#!/usr/bin/env python3

import sys

def solution(A, B, K):
    if A % K == 0:
        return int((B - A) / K + 1)
    else:
        return int((B - (A - A % K)) / K)

if __name__ == '__main__':
    print(solution(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))
