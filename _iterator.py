#!/usr/bin/env python


class Range(object):
    def __init__(self, n):
         self.i = 0
         self.n = n

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()


def main():
    r = Range(3)
    print r.next()
    print r.next()
    print r.next()
    print r.next()


if __name__ == '__main__':
    main()

