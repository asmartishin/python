#!/usr/bin/env python

import sys
words = sys.stdin.readline().split()
count = sys.stdin.readline()
dictionary = sys.stdin.readline().split()

print "Correct" if all(word in d for word in words) else "Misspell"
