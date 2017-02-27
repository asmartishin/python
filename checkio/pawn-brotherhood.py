#!/usr/bin/env python3

from pprint import pprint

FIELD_COLUMNS = {
    'x': {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7},
    'y': {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
}


class PlayingField(object):
    def __init__(self):
        self.field = [x[:] for x in [[False] * 8] * 8]
        self.pawns = []

    def add_pawn(self, x, y):
        self.field[FIELD_COLUMNS['y'][y]][FIELD_COLUMNS['x'][x]] = True
        self.pawns.append((FIELD_COLUMNS['y'][y], FIELD_COLUMNS['x'][x]))

    def is_pawn_safe(self, pawn):
        y = pawn[0]
        x = pawn[1]
        is_safe = False
        if (y + 1) < 8:
            if (x + 1) < 8:
                if self.field[y + 1][x + 1]:
                    is_safe = True
            if (x - 1) >= 0:
                if self.field[y + 1][x - 1]:
                    is_safe = True
        return is_safe


def safe_pawns(pawns):
    result = 0
    playing_filed = PlayingField()
    for pawn in pawns:
        playing_filed.add_pawn(pawn[0], pawn[1])
    for pawn in playing_filed.pawns:
        if playing_filed.is_pawn_safe(pawn):
            result += 1
    return result


if __name__ == '__main__':
    print(safe_pawns(["a1","b2","c3","d4","e5","f6","g7","h8"]))
