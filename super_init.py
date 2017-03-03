#!/usr/bin/env python

class A(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class B(A):
    def __init__(self, z, **kwargs):
        super(B, self).__init__(**kwargs)
        self.z = z
        print (self.x, self.y, self.z)

B(x=4, y=3, z=2)
