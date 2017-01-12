#!/usr/bin/env python

import re

def checkio(text):
    currencies = set(re.findall('\$[0-9.,]*[0-9]', text))
    for currency in currencies:
        new_currency = re.sub(r',([0-9]{0,2}$)', r'.\1', re.sub('\.', ',', currency))
        text = text.replace(currency, new_currency)
    return text

if __name__ == '__main__':
    print(checkio('How are You?'))
