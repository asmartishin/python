#!/usr/bin/env python

from functools import wraps, partial
import logging
from sys import stdout

logger = logging.getLogger(__name__)
logging.basicConfig(stream=stdout, format='%(asctime)s %(levelname)s %(message)s')


class MyException(Exception):
    pass


class AnotherException(Exception):
    pass


def log_exceptions(logger):
    def function_decorator(func):
        @wraps(func)
        def function_wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logger.error(e.message)
                raise e
        return function_wrapper
    return function_decorator


def change_exception_class(old_exception, new_exception, message=None):
    def function_decorator(func):
        @wraps(func)
        def function_wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if isinstance(e, old_exception):
                    if message:
                        raise new_exception(message)
                    raise new_exception(e.message)
                raise e
        return function_wrapper
    return function_decorator


def log_all_exceptions(logger):
    def log_all_exceptions_decorator(cls):
        cls_init = cls.__init__

        def __init__(self, *args, **kwargs):
            cls_init(self, *args, **kwargs)
            for key, value in cls.__dict__.items():
                if callable(value):
                    setattr(cls, key, log_exceptions(logger)(value))

        cls.__init__ = __init__
        return cls
    return log_all_exceptions_decorator


@log_all_exceptions(logger)
class Stat(object):
    @change_exception_class(MyException, AnotherException, 'my test 1')
    def time_it(self):
        raise MyException('test 1')

    def count_workers(self):
        raise MyException('test 2')


if __name__ == '__main__':
    stat = Stat()

    try:
        stat.time_it()
    except Exception as e:
        pass

    try:
        stat.count_workers()
    except Exception as e:
        pass

