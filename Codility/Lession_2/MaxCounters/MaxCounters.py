#!/usr/bin/env python3

def MaxCounter(B):
    m = max(B)
    for i in range(len(B)):
        B[i] = m
    return B

def MinusOne(A):
    for i in range(len(A)):
        A[i] -= 1
    return A

def increase(x):
    return x + 1

def solution(N, A):
    B = []
    for i in range(N):
        B.append(0)

    for i in range(len(A)):
        if 0 <= A[i] <= N - 1:
            B[A[i]] = increase(B[A[i]])
            print(B)
        elif A[i] == N:
            B = MaxCounter(B)
            print(B)
    print(B)

def main():
    A = [3, 4, 4, 6, 1, 4, 4]
    A = MinusOne(A)
    N = 5
    solution(N, A)

main()

