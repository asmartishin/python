#!/usr/bin/env python

import re
from string import ascii_lowercase
from collections import Counter

def checkio(string):
    letter_dict = {}
    pop_letters = []

    string = string.lower()
    only_letters = "".join(re.findall('[a-z]+', string))
    for letter in ascii_lowercase:
        letter_dict[letter] =  only_letters.count(letter)
    sorted_keys = sorted(letter_dict, key = letter_dict.get, reverse = True)
    pop_count = letter_dict[sorted_keys[0]]
    for letter in sorted_keys:
        if letter_dict[letter] == pop_count:
            pop_letters.append(letter)
        else:
            pass
    best_index = len(ascii_lowercase)
    for letter in pop_letters:
        if ascii_lowercase.index(letter) < best_index:
            best_index = ascii_lowercase.index(letter)
        else:
            pass
    return ascii_lowercase[best_index]

#def checkio(text):
#    most_freq = Counter([ch for ch in text.lower() if ch.isalpha()]).most_common()
#    max_freq = most_freq[0][1]
#    most_freq = dict(Counter([ch for ch in text.lower() if ch.isalpha()]).most_common())
#    return sorted([k for k,v in most_freq.iteritems() if v == max_freq])[0]

print(checkio("aaaHelloo world!"))
