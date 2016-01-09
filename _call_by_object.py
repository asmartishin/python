#!/usr/bin/env python
# In python, when you assign a value, you are assigning a name to an object. Objects can be mutable and immutable

def foo1(bar):
    bar.append(42)
    print(bar)

def foo2(bar):
    bar = 'new'
    print(bar)

a = []
foo1(a)
print(a)

b = 'old'
foo2(b)
print(b)


# another example. we are appending to the same object 

x = [[]]*3
x[0].append('a')
x[1].append('b')
x[2].append('c')
x[0]=['d']
print x

#out: 
#[['d'], ['a', 'b', 'c'], ['a', 'b', 'c']]
