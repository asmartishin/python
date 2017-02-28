#!/usr/bin/env python3

import math


def checkio(height, width):
    c = height / 2
    a = width / 2
    area = 0
    volume = 0
    if c < a:
        e = math.sqrt(1 - (c ** 2 / a ** 2))
        area = 2 * math.pi * a ** 2 * (1 + (1 - e ** 2) / e * math.atanh(e))
    elif c == a:
        area = 4 * math.pi * a ** 2
        volume = (4 / 3) * math.pi * a ** 2
    else:
        e = math.sqrt(1 - (a ** 2 / c ** 2))
        area = 2 * math.pi * a ** 2 * (1 + c / (a * e) * math.asin(e))
    volume = (4 / 3) * math.pi * c * (a ** 2)
    return [round(volume, 2), round(area, 2)]


if __name__ == '__main__':
    print(checkio(2, 2))
