#!/usr/bin/env python3

import sys


def scramble(s1, s2):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    s1_dict = {}
    for i in alphabet:
        s1_dict[i] = 0
    for i in s1:
        s1_dict[i] += 1
    for i in s2:
        if s1_dict[i] > 0:
            s1_dict[i] -= 1
        else:
            return False
    return True

def main():
    print(scramble(sys.argv[1], sys.argv[2]))

if __name__ == '__main__':
    main()
