import threading


class RequestContextData(type):
    @property
    def data(cls):
        if hasattr(cls._thread, 'data'):
            return cls._thread.data
        return {}

    @data.setter
    def data(cls, data):
        cls._thread.data = data


class RequestContext(object):
    """
    Usage example:
        with tornado.stack_context.StackContext(functools.partial(RequestContext, data)):
            ...

        with RequestContext(data):
            ...
    """
    __metaclass__ = RequestContextData
    __slots__ = ['_current_data', '_previous_data']

    _thread = threading.local()
    _thread.data = {}

    def __init__(self, data=None):
        if data is None:
            data = {}

        self._current_data = data
        self._previous_data = None

    def __enter__(self):
        self._previous_data = self.__class__.data
        self.__class__.data = self._current_data

    def __exit__(self, type, value, traceback):
        self.__class__.data = self._previous_data
        del self._previous_data
        return False

