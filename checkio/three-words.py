#!/usr/bin/env python

import re


def checkio(words):
    non_numbers = 0
    for word in words.split():
        if re.match(r'^[^0-9]+$', word):
            non_numbers += 1
        else:
            non_numbers = 0
        if non_numbers == 3:
            return True
    return False

if __name__ == '__main__':
    print(checkio("He is 123 man"))
