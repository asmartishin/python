import time

from tornado import gen


class LazyCache(object):
    def __init__(self, callback, log=None, cache_ttl=60):
        self._callback = callback
        self._log = log
        self._cache_ttl = cache_ttl

        self._data = None
        self._cache_expried = 0

    @property
    def data(self):
        if time.time() > self._cache_expried:
            self.refresh()

        return self._data

    def refresh(self):
        try:
            self._refresh()
            self._cache_expried = time.time() + self._cache_ttl
        except Exception as e:
            if self._log:
                self._log.exception('Error, when updating cache: {}'.format(e))

    def _refresh(self):
        self._data = self._callback()


class AsyncLazyCache(LazyCache):
    @gen.coroutine
    def _refresh(self):
        self._data = yield self._callback()
