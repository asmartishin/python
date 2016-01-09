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

# another example. we are appending to the same object 
x = [[]]*3
x[0].append('a')
x[1].append('b')
x[2].append('c')
x[0]=['d']

print x
