#!/usr/bin/env python3

import re


def is_valid_IP(string):
    if re.match("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", string):
        return True
    else:
        return False

print(is_valid_IP('123.45.67.89'))
