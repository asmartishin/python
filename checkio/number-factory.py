#!/usr/bin/env python

import sys


def eratosthenes_sieve(number):
    biggest_divisor = int(number / 2) + 1
    divisors = list(xrange(biggest_divisor))[2:]
    index = 0
    while index < len(divisors):
        divisor = divisors[index]
        multiplier = 2
        while divisor * multiplier < biggest_divisor:
            multiplied_divisor = divisor * multiplier
            if multiplied_divisor in divisors:
                divisors.remove(multiplied_divisor)
            multiplier += 1
        index += 1
    return divisors


def trial_division(number, divisors):
    index = 0
    result = []
    while index < len(divisors) and number > 1:
        divisor = divisors[index]
        if number % divisor == 0:
            number /= divisor
            result.append(divisor)
        else:
            index += 1
    return result if result else [number]


def reduce_divisors(divisors_slice):
    mul_result = 1
    result = []
    for divisor in divisors_slice[::-1]:
        if mul_result * divisor < 10:
            mul_result *= divisor
        else:
            result.append(mul_result)
            mul_result = divisor
    result.append(mul_result)
    return result[::-1]


def checkio(number):
    number = int(number)
    divisors = trial_division(number, eratosthenes_sieve(number))
    print divisors
    if not all(x < 10 for x in divisors):
        return 0
    if 3 in divisors or 2 in divisors:
        if 3 in divisors:
            stop_index = len(divisors) - divisors[::-1].index(3)
        elif 2 in divisors:
            stop_index = len(divisors) - divisors[::-1].index(2)
        return min(
            int(''.join(str(x) for x in sorted(reduce_divisors(divisors[:stop_index]) +  divisors[stop_index:]))),
            int(''.join(str(x) for x in sorted(reduce_divisors(divisors[:stop_index][::-1]) +  divisors[stop_index:])))
        )
    else:
        return int(''.join(str(x) for x in divisors))


if __name__ == '__main__':
    print(checkio(sys.argv[1]))
