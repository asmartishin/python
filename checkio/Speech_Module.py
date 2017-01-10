#!/usr/bin/env python

FIRST_TEN = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
HUNDRED = "hundred"

def checkio(number):
    words = []
    if number >= 100:
        words.append(FIRST_TEN[number // 100])
        words.append(HUNDRED)
        number %= 100
    if number >= 20:
        words.append(OTHER_TENS[number // 10 - 2])
        number %= 10
    if number >= 10:
        words.append(SECOND_TEN[number - 10])
    elif number > 0 or words == []:
        words.append(FIRST_TEN[number])
    return ' '.join(words)

print(checkio(521))
