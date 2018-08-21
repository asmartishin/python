#!/usr/bin/env python

from functools import wraps

class RequiredFieldError(Exception):
    pass

class A(object):
    def _required(*fields):
        def validate_decorator(func):
            @wraps(func)
            def validate_wrapper(self, value):
                for field in fields:
                    if field not in value:
                        raise RequiredFieldError('field {} missinfg from parsed object'.format(field))

                return func(self, value)
            return validate_wrapper
        return validate_decorator

    @_required('b')
    def my_func(self, data):
        print data['b']

    _required = staticmethod(_required)

class B(A):
    @A._required('a')
    def my_func(self, data):
        print data['a']

def main():
    a = A()
    b = B()
    a.my_func({'b': 2})
    b.my_func({'a': 1})

if __name__ == '__main__':
    main()
