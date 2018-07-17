import logging
import sys
from collections import namedtuple

LoggingStreamHandler = namedtuple('LoggingStreamHandler', 'stream levels')


class LoggingLevelFilter(logging.Filter):
    def __init__(self, levels, name=''):
        self._min_level = min(levels)
        self._max_level = max(levels)
        super(LoggingLevelFilter, self).__init__(name)

    def filter(self, record):
        return self._min_level <= record.levelno <= self._max_level


def init_root_logger():
    log = logging.getLogger()
    log.setLevel(logging.INFO)

    for stream_handler in (
            LoggingStreamHandler(sys.stdout, (logging.NOTSET, logging.INFO)),
            LoggingStreamHandler(sys.stderr, (logging.ERROR, logging.CRITICAL))
    ):
        handler = logging.StreamHandler(stream_handler.stream)
        handler.setFormatter(logging.Formatter('%(message)s'))
        handler.addFilter(LoggingLevelFilter(stream_handler.levels))
        log.addHandler(handler)
