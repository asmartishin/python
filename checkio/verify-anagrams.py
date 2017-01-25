#!/usr/bin/env python

import collections
import sys

LETTERS = 'abcdefghijklmnopqrstuvwxyz'


def verify_anagrams_helper(first_word, second_word):
    available_letters = collections.defaultdict(int)
    for letter in first_word:
        letter = letter.lower()
        available_letters[letter] += 1
    for letter in second_word:
        letter = letter.lower()
        if letter in LETTERS and letter in available_letters and available_letters[letter] > 0:
            available_letters[letter] -= 1
        elif letter not in LETTERS:
            pass
        else:
            return False
    return True


def verify_anagrams(first_word, second_word):
    return verify_anagrams_helper(first_word, second_word) and verify_anagrams_helper(second_word, first_word)


if __name__ == '__main__':
    print(verify_anagrams(sys.argv[1], sys.argv[2]))
