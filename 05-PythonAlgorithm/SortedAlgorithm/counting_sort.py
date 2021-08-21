# !/usr/bin/env python
# -*- encoding: utf-8 -*-
# Time  : 2021/04/28 10:45:44
# Theme : 计数排序
# 复杂度分析
# 最坏复杂度: 时间复杂度为 O(n+k)
# 最好复杂度：时间复杂度在 O(n+k)
# 平均复杂度: 时间复杂度为 O(n+k)
import random


def counting_sort(sequence):
    if sequence == []:
        return []
    sequence_len = len(sequence)
    sequence_max = max(sequence)  # 找出待排序的数组中最大的元素
    sequence_min = min(sequence)  # 找出待排序的数组中最小的元素
    counting_arr_length = sequence_max-sequence_min+1
    counting_arr = [0]*counting_arr_length
    for number in sequence:
        counting_arr[number-sequence_min] += 1  # 统计数组中元素出现次数
    for i in range(1, counting_arr_length):  # 计数累加
        counting_arr[i] = counting_arr[i]+counting_arr[i-1]
    ordered = [0]*sequence_len
    for i in range(sequence_len-1, -1, -1):  # 反向填充目标数组
        ordered[counting_arr[sequence[i]-sequence_min]-1] = sequence[i]
        counting_arr[sequence[i]-sequence_min] -= 1
    return ordered


if __name__ == '__main__':
    sequence = [random.randint(1, 10000) for i in range(500)]
    print(sequence)
    print(counting_sort(sequence))
