#!/usr/bin/env python3

BASE = 2


def invert_string(string):
    i = 0
    j = len(string) - 1
    result = list(string)

    while (i < j):
        swap = result[i]
        result[i] = result[j]
        result[j] = swap

        i += 1
        j -= 1

    return ''.join(result)


def base_converter(number, base):
    digits = '0123456789ABCDEF'
    result = ''

    while (number >= 1):
        result += str(number % base)
        number //= base

    return invert_string(result)


def checkio(number):
    return base_converter(number, BASE).count('1')


if __name__ == '__main__':
    print(checkio(4))
