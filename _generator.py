#!/usr/bin/env python


from collections import deque


def numbers():
    number = 1
    while True:
        d = deque(str(number))
        while d:
            yield d.popleft()
        number += 1


def take(n, seq):
    seq = iter(seq)
    result = ''
    try:
        for i in range(n):
            result += seq.next()
    except StopIteration:
        pass
    return result


def main():
    print take(10, numbers())


if __name__ == '__main__':
    main()

