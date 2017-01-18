#!/usr/bin/env python

import re

VOWELS = "aeiouy"
CONSONANTS = "bcdfghjklmnpqrstvwxz"


def checkio(text):
    words = re.findall('[a-zA-z^0-9]+', text)
    print(words)
    is_vowel = True
    is_striped = True
    result = 0
    for word in words:
        is_striped = True
        for i, char in enumerate(word):
            char = char.lower()
            if i == 0:
                if char in VOWELS:
                    is_vowel = True
                elif char in CONSONANTS:
                    is_vowel = False
                else:
                    is_striped = False
            else:
                if char in VOWELS and not is_vowel:
                    is_vowel = True
                elif char in CONSONANTS and is_vowel:
                    is_vowel = False
                else:
                    is_striped = False
        if is_striped and len(word) > 1:
            result += 1
    return result


if __name__ == '__main__':
    print(checkio('1st 2a ab3er root rate'))
    pass
