#!/usr/bin/env python

from sys import stdin, stdout
from heapq import heappush, heappop


def get_water_volume(island):
    m = len(island)
    n = len(island[0])

    visited = [[False] * n for x in xrange(m)]

    heights = []
    volume = 0

    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                heappush(heights, (island[i][j], i, j))
                visited[i][j] = True

    while heights:
        height, i, j = heappop(heights)
        neighbours = ((i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1))

        for i, j in neighbours:
            if i < 0 or i > m - 1 or j < 0 or j > n - 1 or visited[i][j]:
                continue

            if height > island[i][j]:
                volume += height - island[i][j]

            heappush(heights, (max(island[i][j], height), i, j))
            visited[i][j] = True

    return volume


if __name__ == '__main__':
    island = map(lambda x: [int(y) for y in str(x).rstrip().split()], stdin.readlines())

    print(get_water_volume(island))

