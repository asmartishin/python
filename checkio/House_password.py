#!/usr/bin/env python3

def checkio(data):
    isLen = False
    isDigit = False
    isLower = False
    isUpper = False
    if len(data) >= 10:
        isLen = True
    else:
        return False
    for char in data:
        if char.isdigit():
            isDigit = True
        elif char.islower():
            isLower = True
        elif char.isupper():
            isUpper = True
        else:
            pass

    if isLen and isDigit and isLower and isUpper:
        return True
    else:
        return False

print(checkio('123456123456'))
