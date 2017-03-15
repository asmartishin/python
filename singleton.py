#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals


class Singleton(type):
    """
    Singleton metaclass
    """
    def __init__(cls, *args, **kwargs):
        super(Singleton, cls).__init__(*args, **kwargs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance


class Person(object):
    __metaclass__ = Singleton

    def __init__(self, age, gender, name, **kwargs):
        self.age = age
        self.gender = gender
        self.name = name
        self.parameters = kwargs

class Cat(object):
    __metaclass__ = Singleton

    def __init__(self, age, gender, name):
        self.age = age
        self.gender = gender
        self.name = name

if __name__ == '__main__':
    alex = Person(24, 'm', 'Алекс', height=187, weight=95)
    anna = Person(23, 'f',  'Анна')
    vasya = Cat(5, 'm', 'Вася')
    mikey = Cat(4, 'm', 'Микки')
    print(anna.parameters)
    print(mikey.name)
