#!/usr/bin/env python


def index_power(array, n):
    if n > len(array) - 1:
        return -1
    return array[n] ** n


if __name__ == '__main__':
    print(index_power([1, 2, 3, 4], 2))
