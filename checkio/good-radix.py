#!/usr/bin/env python

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def convert_to_decimal(number, radix):
    power = len(number) - 1
    result = 0
    for digit in number:
        result += int(digits.index(digit)) * (radix ** power)
        power -= 1
    return int(result)


def checkio(number):
    number = str(number)
    result = 0
    min_radix = 0
    for digit in number:
        if digits.index(digit) > min_radix:
            min_radix = digits.index(digit) + 1
    for radix in range(min_radix, len(digits) + 1):
        if convert_to_decimal(number, radix) % (radix - 1) == 0:
            result = radix
            break

    return result


if __name__ == '__main__':
    number = str(raw_input())
    print(checkio(number))
