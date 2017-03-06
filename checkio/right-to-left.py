#!/usr/bin/env python


def left_join(phrases):
    return ','.join([x.replace('right', 'left') for x in phrases])

if __name__ == '__main__':
    print(left_join(("left", "right", "left", "stop")))
