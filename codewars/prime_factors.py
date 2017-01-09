#!/usr/bin/env python3

import sys, math

def eratosthenes_sieve(n):
    a = [True] * n
    for i in range(2, n):
        for j in range(i * 2, n, i):
            a[j] = False
    return [i for i in range(2, n) if a[i]]


def prime_factors(n):
    s, i, count, first, n_origin  = '', 0, 0, True, n
    prime_numbers = eratosthenes_sieve(int(math.sqrt(n)))
    print(prime_numbers)
    while n != 1:
        if n % prime_numbers[i] == 0:
            if first:
                s += "({}".format(prime_numbers[i])
                first = False
            n //= prime_numbers[i]
            count += 1
        else:
            i += 1
            if count > 1:
                s += "**{})".format(count)
            elif count == 1:
                s += ")"
            count, first = 0, True
        if i == len(prime_numbers):
            s += "({})".format(n)
            break
    if n == 1:
        s += ")"
    if n == n_origin:
        s = "({})".format(n)
    return s


def main():
    print(prime_factors(int(sys.argv[1])))

if __name__ == "__main__":
    main()
