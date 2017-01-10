#!/usr/bin/env python

def checkio(field):
    for line in field:

        if line.count('X') == 3:
            return('X')
        elif line.count('O') == 3:
            return('O')

    rotated_field = zip(*field)
    for line in rotated_field:
        if line.count('X') == 3:
            return('X')
        elif line.count('O') == 3:
            return('O')

    if field[0][0] == field[1][1] == field[2][2] and field[0][0] != ".":
        return field[0][0]
    elif field[0][2] == field[1][1] == field[2][0] and field[0][2] != ".":
        return field[0][2]
    return "D"

print(checkio([
    "X.O",
    "XX.",
    "XOO"]))
print(checkio([
    "OO.",
    "XOX",
    "XOX"]))
print(checkio([
    "OOX",
    "XXO",
    "OXX"]))
