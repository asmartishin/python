#!/usr/bin/env python


def find_message(text):
    result = ""
    for char in text:
        if char.isupper():
            result += char
    return result

if __name__ == '__main__':
    print(find_message('How are you? Eh, ok. Low or Lower? Ohhh.'))
