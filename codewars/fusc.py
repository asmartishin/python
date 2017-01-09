#!/usr/bin/env python

import sys
import functools

def with_trampoline(f):
    @functools.wraps(f)
    def g(*args, **kwds):
        h = f
        while h is not None:
            h, args, kwds = h(*args, **kwds)
        return args
    return g

def call(f):
    def g(*args, **kwds):
        return f, args, kwds
    return g

def result(value):
    return None, value, None


def fusc(n):
    assert type(n) == int and n >= 0
    if n == 0 or n == 1:
        return n
    elif n % 2 == 0:
        n = n / 2
        return fusc(n)
    else:
        n = (n - 1) / 2
        return fusc(n) + fusc(n + 1)


def fusc2(n):
    acc = 0
    stack = [n]

    while True:
        to_append = []
        to_pop = []
        for i, k in enumerate(stack):
            if k == 0 or k == 1:
                acc += k
                to_pop.append(i)
            elif k % 2 == 0:
                k = k / 2
            else:
                k = (k - 1) / 2
                to_append.append(k + 1)
            stack[i] = k

        j = 0
        for i, k in enumerate(to_pop):
            stack.pop(k - j)
            j += 1

        stack.extend(to_append)

        if len(stack) == 0:
            break
    return acc


def fusc3(n):
    acc = 0
    if n == 0 or n == 1:
        return call(fusc3)(n, acc += n)
    elif n % 2 == 0:
        n = n / 2
        return call(fusc3)(n, acc)
    else:
        n = (n - 1) / 2
        return call(fusc3)(n, acc) + call(fusc3)(n + 1, acc)
    return result(acc)

def trampoline_factorial(n, acc=1):
    if n < 2:
        return result(acc)
    return call(trampoline_factorial)(n - 1, n * acc)


if __name__ == '__main__':
    fusc3_t = with_trampoline(fusc3)
    print(fusc3_t(int(84)))
