#!/usr/bin/env python
# -*- coding: utf-8 -*-

#*args allows you pass an arbitrary number of arguments to function (unknown number)
#**kwargs allows you to handle named arguments, not defined in advance

import inspect

def args_pass(*args):
    print(inspect.stack()[0][3], locals())

def kwargs_pass(**kwargs):
    print(inspect.stack()[0][3], locals())

def args_kwargs_pass(fargs, *args, **kwargs):
    print(inspect.stack()[0][3], locals())

list_test = (1, 'two', 3) #it can be an array
dict_test = {'arg1': 1, 'arg2': 2, 'arg3': 'three'}

args_pass(*list_test)
kwargs_pass(**dict_test)
args_kwargs_pass(1, *list_test, **dict_test)

#out:
#('args_pass', {'args': (1, 'two', 3)})
#('kwargs_pass', {'kwargs': {'arg1': 1, 'arg2': 2, 'arg3': 'three'}})
#('args_kwargs_pass', {'args': (1, 'two', 3), 'fargs': 1, 'kwargs': {'arg1': 1, 'arg2': 2, 'arg3': 'three'}})
