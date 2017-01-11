#!/usr/bin/env python

import sys


def checkio(expression):
    brackets = {
        ')' : '(',
        '}': '{',
        ']' : '['
    }

    stack = []

    open_brackets = brackets.values()
    close_brackets = brackets.keys()

    for char in expression:
        if (char not in open_brackets) and (char not in close_brackets):
            pass
        elif char in open_brackets:
            stack.append(char)
        elif char in close_brackets:
            try:
                if brackets[char] != stack.pop():
                    return False
            except IndexError as e:
                return False
    return False if stack else True


if __name__ == '__main__':
    print(checkio(sys.argv[1]))

