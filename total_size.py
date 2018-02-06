#!/usr/bin/env python

from sys import getsizeof
from itertools import chain


def total_size(data):
    used = set()
    handlers = {
        tuple: iter,
        list: iter,
        dict: lambda x: chain.from_iterable(x.items()),
        set: iter,
    }

    def size(data):
        if id(data) in used:
            return 0

        used.add(id(data))
        result = getsizeof(data)

        try:
            for x in handlers[type(data)](data):
                result += size(x)
        except KeyError:
            pass

        return result

    return size(data)


def main():
    d = {'a': ['b', 'e'], 'c': {'t': 'f'}}
    print(total_size(d))


if __name__ == '__main__':
    main()

