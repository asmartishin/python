#!/usr/bin/env python
# -*- coding: utf-8 -*-

class RevealAccess(object):
    def __init__(self, val, name):
        self.val = val
        self.name = name

    def __get__(self, obj, obj_type):
        print 'Получаю', self.name
        return self.val

    def __set__(self, obj, val):
        print 'Обновляю', self.name
        self.val = val


class MyClass(object):
    x = RevealAccess(3, 'x')


def main():
    m = MyClass()
    print m.x
    m.x = 5
    print m.x


if __name__ == '__main__':
    main()

