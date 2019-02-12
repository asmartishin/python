#!/usr/bin/env python

def mark_process(string):
    def process_decorator(func):
        def process_wrapper(self):
            print string
            func(self)
        return process_wrapper
    return process_decorator


class Base(object):
    @mark_process('Base process wrapper')
    def process(self):
        print 'Base Process'


class Child(Base):
    @mark_process('Child process wrapper')
    def process(self):
        super(Child, self).process()
        print 'Child process'

b = Base()
b.process()

print('---------------------')

c = Child()
c.process()

