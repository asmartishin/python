#!/usr/bin/env python3

#def binarySearch(alist, item):
#    first = 0
#    last = len(alist) - 1
#    found = False
#    while first <= last and not found:
#        midpoint = (first + last) // 2
#        if alist[midpoint] == item:
#            found = True
#        else:
#            if item < alist[midpoint]:
#                last = midpoint - 1
#            else:
#                first = midpoint + 1
#    return found

#def binarySearch(alist, item):
#    if len(alist) == 0:
#        return False
#    else:
#        midpoint = len(alist) // 2
#        if alist[midpoint] == item:
#            return True
#        else:
#            if item < alist[midpoint]:
#                return binarySearch(alist[:midpoint], item)
#            else:
#                return binarySearch(alist[midpoint+1:], item)
#
def binarySearch(alist, item, *args):
    if not args:
        first = 0
        last = len(alist) - 1
    else:
        first = args[0]
        last = args[1]
    midpoint = (first + last) // 2
    if alist[midpoint] == item:
        return True
    elif first == last:
        return False
    elif item < alist[midpoint]:
        return binarySearch(alist, item, first, midpoint)
    else:
        return binarySearch(alist, item, midpoint + 1, last)

testlist = [1, 2]
print(binarySearch(testlist, 2))
print(binarySearch(testlist, 13))
