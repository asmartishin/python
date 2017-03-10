#!/usr/bin/env python


def checkio(number):
    return reduce(lambda result, x: result * (x if x else 1), [int(x) for x in str(number)], 1)

if __name__ == '__main__':
    print(checkio(123405))
