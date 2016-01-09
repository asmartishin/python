#!/usr/bin/env python
# In python, when you assign a value, you are assigning a name to an object. Objects can be mutable and immutable

def foo(bar):
    bar.append(42)
    print(bar)

a = []
foo(a)
print(a)

def foo(bar):
    bar = 'new'
    print(bar)

a = 'old'
foo(a)
print(a)
