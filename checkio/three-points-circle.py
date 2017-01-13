#!/usr/bin/env python3

import re
import math


def checkio(data):
    x1, y1, x2, y2, x3, y3 = [
        int(x) for x in sum(list(map(lambda x: x.split(','), re.findall(r'[0-9]+,[0-9+]', data))), [])
    ]

    a1 = x2 - x1
    b1 = y2 - y1
    c1 = (x2 - x1) * (x2 + x1) / 2 + (y2 - y1) * (y2 + y1) / 2

    a2 = x3 - x1
    b2 = y3 - y1
    c2 = (x3 - x1) * (x3 + x1) / 2 + (y3 - y1) * (y3 + y1) / 2

    xC = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
    yC = (a1 * c2 - a2 * c1) / (a1 * b2 - a2 * b1)

    r = math.sqrt((xC - x1) ** 2 + (yC - y1) ** 2)

    return '(x-{})^2+(y-{})^2={}^2'.format(
        str(round(xC, 2)).rstrip('.0'),
        str(round(yC, 2)).rstrip('.0'),
        str(round(r, 2)).rstrip('.0')
    )

if __name__ == '__main__':
    print(checkio('(2,2),(6,2),(2,6)'))
