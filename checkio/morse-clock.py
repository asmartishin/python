#!/usr/bin/env python


def to_binary(number, size):
    binary = []
    number = int(number)
    while number > 0:
        binary.append(number % 2)
        number /= 2
    result = ''.join(reversed([str(x) for x in binary]))
    if len(result) < size:
        for i in xrange(len(result), size):
            result = '0' + result
    return result

def checkio(time_string):
    time = [list(x) for x in time_string.split(':')]
    for i, v in enumerate(time):
        if len(v) == 1:
            time[i].append(time[i][0])
            time[i][0] = '0'
    binary = to_binary(time[0][0], 2) + ' ' + to_binary(time[0][1], 4) + \
        ' : ' + to_binary(time[1][0], 3) + ' ' + to_binary(time[1][1], 4) + \
        ' : ' + to_binary(time[2][0], 3) + ' ' + to_binary(time[2][1], 4)
    result = list(binary)
    for i, v in enumerate(binary):
        if v == '1':
            result[i] = '-'
        elif v == '0':
            result[i] = '.'
    return ''.join(result)

if __name__ == '__main__':
    print(checkio('00:1:02'))
