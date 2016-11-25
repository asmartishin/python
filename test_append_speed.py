#!/usr/bin/env python

import timeit
import random
import string
import os
import binascii


def random_hash():
    return binascii.hexlify(os.urandom(8))


def random_character():
    return random.choice(string.ascii_letters)


def a():
    result = []
    for i in range(10):
        result.append({random_hash(): random_character()})
        if not (i % 2):
            result[-1][random_hash()] = random_character()
    return result


def b():
    result = []
    for i in range(10):
        data = {random_hash(): random_character()}
        if not (i % 2):
            data[random_hash()] = random_character()
        result.append(data)
    return result


if __name__ == '__main__':
    print(timeit.timeit("a()", number=1000, setup="from __main__ import a"))
    print(timeit.timeit("b()", number=1000, setup="from __main__ import b"))
