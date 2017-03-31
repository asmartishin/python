#!/usr/bin/env python


def capture(matrix):
    seconds = 0
    connections = {x: [] for x in xrange(len(matrix))}
    powers = [0] * len(matrix)

    for y, row in enumerate(matrix):
        for x, el in enumerate(row):
            if x == y:
                powers[y] = matrix[y][x]
            elif matrix[y][x] == 1:
                connections[y].append(x)

    queue = set(connections[0])

    while queue:
        queue_snap = list(queue)
        for computer in queue_snap:
            powers[computer] -= 1
            if powers[computer] == 0:
                queue.remove(computer)
                for connected_computer in connections[computer]:
                    if powers[connected_computer] > 0:
                        queue.add(connected_computer)
        seconds += 1
    return seconds


if __name__ == '__main__':
    print(capture([[0, 1, 0, 1, 0, 1],
                    [1, 8, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]))
