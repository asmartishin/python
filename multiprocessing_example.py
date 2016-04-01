from multiprocessing.dummy import Pool
from multiprocessing import cpu_count

# not a good example)
def f(n, m):
    fr = lambda x, y: x + y
    fm = lambda x: x if x < m else x % m
    pool = Pool(cpu_count())
    result = reduce(fr, pool.map(fm, xrange(n + 1)))
    pool.close()
    pool.join()
    return result

print(f(9927331, 5219912))
