#!/usr/bin/env python

import string
import random

def generate_random_string(chars, size):
    return  ''.join(random.choice(chars) for _ in xrange(size))

if __name__ == '__main__':
    print generate_random_string(string.ascii_lowercase, 10)

