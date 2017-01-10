#!/usr/bin/env python3

def into(A):
    A = sorted(A)
    a = 1
    for i in range(len(A)):
        print (str(A[i]) + ' ' + str(i + 1))
        if (int(A[i]) != (i + 1)):
            a = 0
            break
    print (a)

if __name__ == '__main__':
    A = [1, 3, 2]
    into(A)
