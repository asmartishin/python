#!/usr/bin/env python


def multiply(*args):
    return reduce(lambda result, x: result * x, args, 1)


def multiply_on(*nargs):
    def _decorated(func):
        def _wrapper(*args, **kwargs):
            return func(*(nargs + args), **kwargs)
        return _wrapper
    return _decorated


@multiply_on(*(4, 1))
def multiply_on_4(*args):
    return multiply(*args)


if __name__ == '__main__':
    print(multiply_on_4(5, 2))
