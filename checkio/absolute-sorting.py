#!/usr/bin/env python

def checkio(numbers_array):
    abs_numbers_dict = {abs(x): x for x in numbers_array}
    return [abs_numbers_dict[x] for x in sorted(abs_numbers_dict)]

if __name__ == '__main__':
    print(checkio((-1, -2, -3, 0)))
