import time


def time_exec(method):
    def timed(*args, **kwargs):
        time_start = time.time()
        result = method(*args, **kwargs)
        time_end = time.time()
        print('{}: {} s'.format(method.__name__, time_end - time_start))
        return result
    return timed
