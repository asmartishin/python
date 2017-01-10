#!/usr/bin/env python3

def checkio(data):
    tmp_array = []
    for i in data:
        if data.count(i) > 1:
            tmp_array.append(i)
    data = tmp_array
    return data

print(checkio([10, 9, 10, 10, 9, 8]))
