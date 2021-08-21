#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Time  : 2021/05/12 13:25:53
# Theme : 二分查找
# ❖所以二分法查找的算法复杂度是O(log n)

def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint -1
            else:
                first = midpoint +1
    return found
test = [0, 2, 8, 13, 17, 19, 32, 42, 50]
print(binarySearch(test, 3))
print(binarySearch(test, 19))
