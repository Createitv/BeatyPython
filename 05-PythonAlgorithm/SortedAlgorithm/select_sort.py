# !/usr/bin/env python
# -*- encoding: utf-8 -*-
# Time  : 2021/04/28 10:25:32
# Theme : 选择排序
# 但选择排序对交换进行了削减，相比起冒泡排序进行多次交换，每趟仅进行1次交换，记录最大项的所在位置，最后再跟本趟最后一项交换
# 复杂度分析
# 最坏复杂度:时间复杂度为O(n^2)
# 最好复杂度：时间复杂度为O(n^2)
# 平均复杂度:时间复杂度为O(n^2)
def select_sort(sequence):
    """
    选择排序（Selection sort）是一种简单直观的排序算法。它的工作原理是：第一次从待排序的数据元素中选出最小（或最大）的一个元素，存放在序列的起始位置，然后再从剩余的未排序元素中寻找到最小（大）元素，然后放到已排序的序列的末尾。以此类推，直到全部待排序的数据元素的个数为零。选择排序是不稳定的排序方法。
    """
    for i in range(len(sequence) - 1):
        minIndex = i
        for j in range(i + 1, len(sequence)):
            if sequence[j] < sequence[minIndex]:
                minIndex = j
        sequence[minIndex], sequence[i] = sequence[i], sequence[minIndex]
    return sequence


print(select_sort([21, 3, 4, 5, 2, 32, 12, 13, 31]))
