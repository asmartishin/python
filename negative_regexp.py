#!/usr/bin/env python

import re


def main(letters):
    do_not_like = re.compile('^((?!like).)*$')
    return [x for x in letters if do_not_like.match(x)]


if __name__ == '__main__':
    letters = ['You hate cs', "he like's cs", 'I like cs']
    print(main(letters))
