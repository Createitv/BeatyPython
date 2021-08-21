# !/usr/bin/env python
# -*- encoding: utf-8 -*-
# Time  : 2021/04/28 10:42:14
# Theme : 快速排序
# 最坏复杂度: 时间复杂度为 O(n ^ 2)
# 最好复杂度：时间复杂度在 O(n) 和 O(nlogn)中间
# 平均复杂度: 时间复杂度为 O(nlogn)
'''
快速排序的思路是依据一个“中值”数据 项来把数据表分为两半:小于中值的一半 和大于中值的一半，然后每部分分别进行快速排序(递归)
'''


def quicksort(array):
    """easy read"""
    if len(array) < 2:
        # base case, arrays with 0 or 1 element are already "sorted"
        return array
    else:
        # recursive case
        pivot = array[0]
        # sub-array of all the elements less than the pivot
        less = [i for i in array[1:] if i <= pivot]
        # sub-array of all the elements greater than the pivot
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([10, 5, 2, 3]))
