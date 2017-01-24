#!/usr/bin/env python3

import math


def checkio(a, b, c):
    if a + b <= c or a + c <= b or c + b <= a:
        return [0, 0, 0]
    alpha = round(math.degrees(math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c))))
    betta = round(math.degrees(math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))))
    gamma = round(math.degrees(math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))))
    return sorted([alpha, betta, gamma])


if __name__ == '__main__':
    print(checkio(2, 2, 5))

