#!/usr/bin/env python3

#*args allows you pass an arbitrary number of arguments to function (unknown number)
#**kwargs allows you to handle named arguments, not defined in advance

import inspect

def test_var_args(farg, *args):
    print(inspect.stack()[0][3], locals())
    print("formal arg:", farg)
    for arg in args:
        print("another arg:", arg)

def test_var_kwargs(farg, **kwargs):
    print(inspect.stack()[0][3], locals())
    print("formal arg: ", farg)
    for key in kwargs:
        print("another keyword arg: %s: %s" % (key, kwargs[key]))

def var_list_call(arg1, arg2, arg3):
    print(inspect.stack()[0][3], locals())
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

def var_dic_call(arg1, arg2, arg3):
    print(inspect.stack()[0][3], locals())
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

var_dic = {"arg3": 3, "arg2": "two"}
var_list = ("two", 3)

var_list_call(1, *var_list)
var_list_call(*['uno', 'des', 'tres'])
var_dic_call(1, **var_dic)
var_dic_call(**{"arg1": "uno", "arg2": "dos", "arg3": "tres"})
test_var_args(1, "two", 3)
test_var_kwargs(farg=1, myarg2="two", myarg3=3)

