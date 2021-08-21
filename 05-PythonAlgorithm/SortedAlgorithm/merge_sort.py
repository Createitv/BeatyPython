# !/usr/bin/env python
# -*- encoding: utf-8 -*-
# Time  : 2021/04/28 10:40:28
# Theme : 归并排序
# 复杂度分析
# 最坏复杂度: 时间复杂度为 O(nlogn)
# 最好复杂度：时间复杂度为 O(nlogn)
# 平均复杂度: 时间复杂度为 O(nlogn)
import math

def merge_sort(sequence):
    if(len(sequence) < 2):
        return sequence
    mid = math.floor(len(sequence)/2)
    left, right = sequence[0:mid], sequence[mid:]
    return merged(merge_sort(left), merge_sort(right))


def merged(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result

# another way
def merge_sort2(lst):
    if len(lst) <= 1:
        return lst

    # divide qusiton
    middle = len(lst) // 2
    left = merge_sort2((lst[:middle]))
    right = merge_sort2(lst[middle:])
    merged = []
    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(right if right else left)
    return merged
