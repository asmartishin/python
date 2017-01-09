#!/usr/bin/env python

def regressionLine(x, y):
    b = ((len(x) * sum(map(lambda x: x[0] * x[1], zip(x, y)))) - sum(x) * sum(y)) / float(len(x) * sum(map(lambda x: x ** 2, x)) - (sum(x)) ** 2)
    a = (sum(y) - b * (sum(x))) / float(len(x))
    return float('{0:.4f}'.format(a)), float('{0:.4f}'.format(b))

print(regressionLine([25,30,35,40,45,50], [78,70,65,58,48,42]))
