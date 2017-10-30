#!/usr/bin/env python

import argparse
import os
import re
import sys


def parse_arguments():
    def valid_file(filename):
        if not os.path.exists(filename):
            raise argparse.ArgumentTypeError('File {} does not exist'.format(filename))
        return filename
    parser = argparse.ArgumentParser(description='Script for parsing CMakeLists.txt for clion')
    parser.add_argument('-f', '--filename', type=valid_file, required=True, help='CMakeLists.txt file')
    return vars(parser.parse_args())


def main(*args, **options):
    filename = options.get('filename')

    with open(filename, 'r') as f:
        for line in f.readlines():
            found = re.search(r'[a-zA-z/0-9\-]+\.[hcp]{1,3}', line)
            if found and not os.path.exists(found.group(0)):
                continue

            sys.stdout.write(line)


if __name__ == '__main__':
    main(**parse_arguments())

