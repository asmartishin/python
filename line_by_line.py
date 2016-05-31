#!/usr/bin/env python

import re

dictinary = {re.search('^([0-9.]+)\t([A-Z_]+)', line.rstrip('\n')).group(2):re.search('^([0-9.]+)\t([A-Z_]+)', line.rstrip('\n')).group(1) for line in open('values.txt')}

with open('template_out.txt', 'w') as out_file:
    for line in open('template.txt'):
        if re.search('"name": "([A-Z_]+)"', line):
            group_name = re.search('"name": "([A-Z_]+)"', line).group(1)
            current_value = dictinary[group_name]
        if  re.search('"foo"|"bar"|"foo_bar"|"bar_foo"', line):
            line = re.sub('[0-9.]+', current_value, line)
        out_file.write(line)
