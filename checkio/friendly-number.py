#!/usr/bin/env python3

import math


def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    power_suffix = powers[0]
    counter = 1
    number = float(number)
    while math.fabs(number) >= base:
        if counter < len(powers):
            power_suffix = powers[counter]
        else:
            break
        number /= base
        counter += 1
    if decimals == 0:
        if number >= 0:
            number = math.floor(number)
        else:
            number = math.ceil(number)
    else:
        number = round(number, decimals)
    number = str(number)
    if len(number.split('.')) > 1:
        decimal_part = number.split('.')[1]
    else:
        decimal_part = ''
    if len(decimal_part) < decimals:
        if not decimal_part:
            number += '.'
        for i in range(len(decimal_part), decimals):
            number += '0'
    return number + power_suffix + suffix


if __name__ == '__main__':
    print(friendly_number(10**32))
