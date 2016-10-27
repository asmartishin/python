#!/usr/bin/env python3

import os
import binascii
from pprint import pprint
import time

def random_hash():
    return binascii.b2a_hex(os.urandom(16)).decode("utf-8")

add_attr_lam = lambda x: x.update({random_hash(): random_hash()}) or x

def add_attr_func(x):
    key = random_hash()
    x[key] = random_hash()
    return x.copy()

def time_exec(method):
    def timed(*args, **kwargs):
        time_start = time.time()
        result = method(*args, **kwargs)
        time_end = time.time()
        print('{}: {} s'.format(method.__name__, time_end - time_start))
        return result
    return timed

@time_exec
def test_lam(dict_lam):
    return list(map(lambda x: add_attr_lam(x), dict_lam))

@time_exec
def test_func(dict_func):
    return list(map(lambda x: add_attr_func(x), dict_func))

dict_lam = []
dict_func = []
for j in range(100):
    dict_lam.append({random_hash(): random_hash() for i in range(100)})
    dict_func.append({random_hash(): random_hash() for i in range(100)})
test_lam(dict_lam)
test_func(dict_func)
