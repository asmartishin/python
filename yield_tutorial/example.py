#!/usr/bin/env python

def foo():
    for i in xrange(4):
        yield i

for i in foo():
    print i
