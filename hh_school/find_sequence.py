#!/usr/bin/env python

from sys import stdin, stdout
from collections import deque


def generate_string():
    number = 1
    while True:
        d = deque(str(number))
        while d:
            yield d.popleft()
        number += 1


def find_sequence(A):
    n = len(A)

    prefix = compute_prefix(A)
    p = 0

    for i, l in enumerate(generate_string()):
        while p > 0 and A[p] != l:
            p = prefix[p - 1]

        if A[p] == l:
            p += 1

        if p == n:
            return i - n + 2


def compute_prefix(A):
    n = len(A)

    prefix = [0] * n

    for i in range(1, n):
        p = prefix[i - 1]
        while p > 0 and A[p] != A[i]:
            p = prefix[p - 1]

        if A[p] == A[i]:
            p += 1
        prefix[i] = p
    return prefix


if __name__ == '__main__':
    for i in map(lambda x: str(x).rstrip(), stdin.readlines()):
        print(find_sequence(i))

