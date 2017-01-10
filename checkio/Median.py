#!/usr/bin/env python3

def checkio(data):
    data.sort()
    length = len(data)
    if length % 2 == 0:
        #print("even")
        return ((data[int(length / 2) - 1] + data[int(length / 2)]) / 2)
    else:
        #print("odd")
        return (data[int(((length - 1) / 2))])

print(checkio([6,5,4,3,2,1]))
