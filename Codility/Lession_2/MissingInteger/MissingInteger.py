#!/usr/bin/env python3

def solution(A):
    a = set(A)
    t = 0
    m = max(a)
    for i in a:
        if i != t + 1:
            print(t + 1)
            break
        elif i == m:
            print(i)
        else:
            t = i

solution([])
