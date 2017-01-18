#!/usr/bin/env python

from pprint import pprint

def rotate_matrix(matrix):
    length = len(matrix)
    result = [['.'] * length for i in range(length)]
    for y, row in enumerate(matrix):
        for x, el in enumerate(row):
            result[x][length - 1 - y] = el
    return result


def recall_password(cipher_grille, ciphered_password):
    result = ''
    for rotations in xrange(4):
        for y, row in enumerate(ciphered_password):
            for x, el in enumerate(row):
                if cipher_grille[y][x] == 'X':
                    result += el
        cipher_grille = rotate_matrix(cipher_grille)
    return result


if __name__ == '__main__':
    print(recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')))
