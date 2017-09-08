#!/usr/bin/env python

import math
from sys import stdin, stdout


def min_value(hist, i, j):
    if (i == -1):
        return j

    if (j == -1):
        return i

    return i if hist[i] < hist[j] else j


def rmq(hist, st, ss, se, qs, qe, i):
    if qs <= ss and qe >= se:
        return st[i]

    if se < qs or ss > qe:
        return -1

    m = (ss + se) / 2

    return min_value(
        hist,
        rmq(hist, st, ss, m, qs, qe, 2 * i + 1),
        rmq(hist, st, m + 1, se, qs, qe, 2 * i + 2)
    )


def create_segment_tree(hist, st, s, e, i):
    if (s == e):
        st[i] = s
        return st[i]

    m = (s + e) / 2

    st[i] = min_value(
        hist,
        create_segment_tree(hist, st, s, m, i * 2 + 1),
        create_segment_tree(hist, st, m + 1, e, i * 2 + 2)
    )
    return st[i]


def get_max_rectangle_area(hist, st, n, s, e):
    if (s > e):
        return -1

    if (s == e):
        return hist[s]

    m = rmq(hist, st, 0, n - 1, s, e, 0)

    return max(
        get_max_rectangle_area(hist, st, n, s, m - 1),
        get_max_rectangle_area(hist, st, n, m + 1, e),
        (e - s + 1) * (hist[m])
    )


def largest_histogram(histogram):
    n = len(histogram)
    st_size  = 2 * math.pow(2, math.ceil(math.log(n, 2))) - 1
    st = [None for x in range(int(st_size))]
    create_segment_tree(histogram, st, 0, n - 1, 0);

    return get_max_rectangle_area(histogram, st, n, 0, n - 1)


if __name__ == '__main__':
    values = map(int, stdin.readline().rstrip().split())
    print(largest_histogram(values))
