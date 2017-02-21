#!/usr/bin/env python

VOWELS = "aeiouy"


def translate(phrase):
    phrase = map(lambda x: list(x), phrase.split(' '))
    result = ''
    for word in phrase:
        while word:
            letter = word[0]
            if letter in VOWELS:
                result += letter
                del word[:3]
            else:
                result += letter
                del word[:2]
        result += ' '
    return result.rstrip()


if __name__ == '__main__':
    print(translate("hoooowe yyyooouuu duoooiiine"))
