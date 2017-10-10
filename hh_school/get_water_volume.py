#!/usr/bin/env python

from sys import stdin, stdout
from heapq import heappush, heappop


def get_water_volume(island):
    n = len(island[0])
    m = len(island)

    visited = [[False] * n for x in xrange(m)]

    heights = []
    volume = 0

    for x in range(n):
        for y in range(m):
            if x == 0 or y == 0 or x == n - 1 or y == m - 1:
                heappush(heights, (island[y][x], x, y))
                visited[y][x] = True

    while heights:
        height, x, y = heappop(heights)
        neighbours = ((x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1))

        for x, y in neighbours:
            if x < 0 or x > n - 1 or y < 0 or y > m - 1 or visited[y][x]:
                continue

            if height > island[y][x]:
                volume += height - island[y][x]

            heappush(heights, (max(island[y][x], height), x, y))
            visited[y][x] = True

    return volume


if __name__ == '__main__':
    island = map(lambda x: [int(y) for y in str(x).rstrip().split()], stdin.readlines())

    print(get_water_volume(island))

