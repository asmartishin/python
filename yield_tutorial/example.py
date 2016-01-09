#!/usr/bin/env python

import math

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False

#def get_primes(input_list):
#    return (element for element in input_list if is_prime(element))

def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1

def get_primes_send(number):
    while True:
        if is_prime(number):
            number = yield number
        number += 1

def solve_number_10():
    total = 2
    for next_prime in get_primes(3):
        if next_prime < 2000000:
            total += next_prime
        else:
            print(total)
            return

def print_successive_primes(iterations, base = 10):
    prime_generator = get_primes_send(base)
    prime_generator.send(None)
    for power in range(iterations):
        print(prime_generator.send(base ** power))

if __name__ == '__main__':
#    solve_number_10()
    print_successive_primes(2)
    
#Simplifying. But remember that yield is a generator
#1) Insert a line result = [] at the start of the function.
#2) Replace each yield expr with result.append(expr).
#3) Insert a line return result at the bottom of the function.
#4) Yay - no more yield statements! Read and figure out code.
#5) Compare function to original definition.
