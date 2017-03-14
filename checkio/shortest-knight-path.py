#!/usr/bin/env python3

import collections
from pprint import pprint

FIELD_COLUMNS = {
    'x': {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7},
    'y': {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
}


def possible_moves(y, x):
    result = []
    if y - 2 >= 0 and x + 1 < 8:
        result.append((y - 2, x + 1))
    if y - 2 >= 0 and x - 1 >= 0:
        result.append((y - 2, x -1))
    if y - 1 >= 0 and x + 2 < 8:
        result.append((y - 1, x + 2))
    if y + 1 < 8 and x + 2 < 8:
        result.append((y + 1, x + 2))
    if y + 2 < 8 and x + 1 < 8:
        result.append((y + 2, x + 1))
    if y + 2 < 8 and x - 1 >= 0:
        result.append((y + 2, x - 1))
    if y + 1 < 8 and x - 2 >= 0:
        result.append((y + 1, x - 2))
    if y - 1 >= 0 and x - 2 >= 0:
        result.append((y - 1, x - 2))
    return result


def checkio_helper(chess_field, y, x):
    queue = collections.deque([[(y, x)]])
    moves = 0
    while queue:
        positions = queue.popleft()
        possible_positions = []
        for position in positions:
            if chess_field[position[0]][position[1]] == 'r':
                return moves
            possible_positions.extend(possible_moves(position[0], position[1]))
        queue.append(possible_positions)
        moves += 1


def checkio(cells):
    result = 0
    cells = list(map(lambda x: list(x), cells.split('-')))
    chess_field = [x[:] for x in [['*'] * 8] * 8]
    chess_field[FIELD_COLUMNS['y'][cells[1][1]]][FIELD_COLUMNS['x'][cells[1][0]]] = 'r'
    chess_field[FIELD_COLUMNS['y'][cells[0][1]]][FIELD_COLUMNS['x'][cells[0][0]]] = 'h'
    result = checkio_helper(chess_field, FIELD_COLUMNS['y'][cells[0][1]], FIELD_COLUMNS['x'][cells[0][0]])
    return result


if __name__ == '__main__':
    print(checkio("h1-g2"))
