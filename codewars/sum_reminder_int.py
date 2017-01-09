from multiprocessing.dummy import Pool
from multiprocessing import cpu_count

def f(n, m):
    fr = lambda x, y: x + y
    fm = lambda x: x if x < m else x % m
    pool = Pool(cpu_count())
    result = reduce(fr, pool.map(fm, xrange(n + 1)))
    pool.close()
    pool.join()
    return result

    #return Math.floor(n / m) * m * (m - 1) / 2 + (n % m) * (n % m + 1) / 2

print(f(9927331, 5219912))