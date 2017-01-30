#!/usr/bin/env python3


def checkio(lines_list):
    size = 4
    matrix = []
    result = 0
    lines = [set(x) for x in lines_list]
    for y in range(size):
        matrix.append([])
        for x in range(size):
            matrix[-1].append(y * size + x + 1)

    for s in range(1, size):
        for y in range(size - s):
            for x in range(size - s):
                if all(set((matrix[y][x + i], matrix[y][x + i + 1])) in lines for i in range(0, s))\
                    and all(set((matrix[y + i][x], matrix[y + i + 1][x])) in lines for i in range(0,s))\
                    and all(set((matrix[y + i][x + s], matrix[y + i + 1][x + s])) in lines for i in range(0,s))\
                    and all(set((matrix[y + s][x + i], matrix[y + s][x + i + 1])) in lines for i in range(0,s)):
                        result += 1
    return result


if __name__ == '__main__':
    print(checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
            [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
            [10, 14], [12, 16], [14, 15], [15, 16]]))
