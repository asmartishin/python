#!/usr/bin/env python

import logging
import logging.config
import functools
from contextlib import contextmanager
import json


class CustomAdapter(logging.LoggerAdapter):
    def __init__(self, logger, request_id, **kwargs):
        self.request_id = request_id
        self.request_info = None

        if kwargs:
            self.request_info = json.dumps({k: v for k, v in kwargs.iteritems() if v})

        super(CustomAdapter, self).__init__(logger, kwargs)

    def process(self, msg, kwargs):
        if self.request_info:
            return '%s {"request": %s, "info": %s}' % (self.request_id, json.dumps(msg), self.request_info), kwargs

        return '[%s] %s' % (self.request_id, msg), kwargs


logger = logging.getLogger(__name__)
console = logging.StreamHandler()
console.setFormatter(logging.Formatter(
    '[%(asctime)s] [%(levelname)s] %(message)s',
    datefmt='%d/%m/%Y:%H:%M:%S')
)
logger.addHandler(console)
logger.setLevel(logging.DEBUG)


class AProxy(object):
    def __init__(self, stat, log):
        self.stat = stat
        self.log = log

    def __getattr__(self, name):
        def wrapper(*args, **kwargs):
            method = getattr(self.stat, name)
            if name == 'foo':
                kwargs['log'] = self.log
            return method(*args, **kwargs)
        return wrapper


class A(object):
    def __init__(self, log):
        self.log = log

    def foo(self, log=None):
        log = log if log else self.log
        log.info('asd')
        return 1


if __name__ == '__main__':
    log = functools.partial(
        lambda l, rid, data=None:
        CustomAdapter(l, rid, **data) if data
        else CustomAdapter(l, rid),
        logger
    )

    a = A(log(1))
    ap = AProxy(a, log(3))
    print ap.foo()
