#!/usr/bin/env python3

A = [2, 3, 1, 5]

def solution_old(A):
    A = sorted(A)
    for i in range(1, len(A)):
        if A[i] != (A[i - 1] + 1):
            print (A[i] - 1)

def solution(A):
    a = set(range(1, max(A) + 1)) - set(A)
    print (a.pop())

if __name__ == '__main__':
    solution(A)
