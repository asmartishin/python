#!/usr/bin/env python

from sys import stdin, stdout


def dfs(island, i, j, m, n, possible_height, visited):
    visited.add((i, j))

    if i == 0 or j == 0 or i == m - 1 or j == n - 1:
        return True

    neighbours = ((i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1))

    for i, j in neighbours:
        if i < 0 or i > m - 1 or j < 0 or j > n - 1:
            continue

        if (i, j) not in visited and possible_height >= island[i][j]:
            return dfs(island, i, j, m, n, possible_height, visited)

    return False


def get_volume(island, i, j, m, n):
    min_height = 1
    max_height = 1001

    while min_height < max_height:
        possible_height = (min_height + max_height) / 2

        visited = set()

        if dfs(island, i, j, m, n, possible_height, visited):
            max_height = possible_height
        else:
            min_height = possible_height + 1

    return possible_height - island[i][j]


def get_water_volume(island):
    m = len(island)
    n = len(island[0])

    volume = 0

    for i in range(1, m - 1):
        for j in range(1, n - 1):
            volume += get_volume(island, i, j, m, n)

    return volume

if __name__ == '__main__':
    island = map(lambda x: [int(y) for y in str(x).rstrip().split()], stdin.readlines())

    print(get_water_volume(island))
