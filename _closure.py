#!/usr/bin/env python
# -*- coding: utf-8 -*-


def outer():
    d = [0]
    def inner():
        d[0] += 1
        return d[0]
    return inner


def main():
    f = outer()
    print(f(), f(), f())


if __name__ == '__main__':
    main()

