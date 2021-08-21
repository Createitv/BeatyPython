# !/usr/bin/env python
# -*- encoding: utf-8 -*-
# Time  : 2021/04/28 10:12:46
# Theme : 冒泡排序
# 复杂度分析
# 最坏复杂度: 时间复杂度为 O(n ^ 2)
# 最好复杂度：时间复杂度为 O(n)
# 平均复杂度: 时间复杂度为 O(n ^ 2)
def bubble_sort(sequence):
    for i in range(1, len(sequence)):
        for j in range(0, len(sequence) - i):
            if sequence[j] > sequence[j + 1]:
                sequence[j], sequence[j + 1] = sequence[j + 1], sequence[j]
    return sequence


def bubble_sort2(alist):
    for j in range(len(alist) - 1, 0, -1):
        for i in range(j):
            if alist[i] > alist[j]:
                alist[i], alist[j] = alist[j], alist[i]
    return alist


alist = [54, 23, 32, 432, 543, 57, 5, 324, 23, 4, 2]
print(bubble_sort2(alist))
