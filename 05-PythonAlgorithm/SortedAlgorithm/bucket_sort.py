# !/usr/bin/env python
# -*- encoding: utf-8 -*-
# Time  : 2021/04/28 10:47:42
# Theme : 桶排序
# 复杂度分析
# 最坏复杂度: 时间复杂度为 O(n+k)
# 最好复杂度：时间复杂度在 O(n)
# 平均复杂度: 时间复杂度为 O(n)
import math
import random
DEFAULT_BUCKET_SIZE = 5


def insertion_sort(sequence):
    for index in range(1, len(sequence)):
        while(index > 0 and sequence[index-1] > sequence[index]):
            sequence[index], sequence[index -
                                      1] = sequence[index-1], sequence[index]
            index = index-1
    return sequence


def bucket_sort(sequence, bucketSize=DEFAULT_BUCKET_SIZE):
    if(len(sequence) == 0):
        return []
    minValue = sequence[0]
    maxValue = sequence[0]
    for i in range(0, len(sequence)):
        if sequence[i] < minValue:
            minValue = sequence[i]  # 寻找最小值
        elif sequence[i] > maxValue:
            maxValue = sequence[i]  # 寻找最大值
    bucketCount = math.floor((maxValue - minValue) / bucketSize) + 1  # 桶的初始化
    buckets = []
    for i in range(0, bucketCount):
        buckets.append([])
    for i in range(0, len(sequence)):  # 遍历数据，将数据依次放进桶中
        buckets[math.floor((sequence[i] - minValue) /
                           bucketSize)].append(sequence[i])
    sortedArray = []
    for i in range(0, len(buckets)):  # 将每一个不是空的桶进行排序
        insertion_sort(buckets[i])
        for j in range(0, len(buckets[i])):
            sortedArray.append(buckets[i][j])
    return sortedArray


if __name__ == '__main__':
    sequence = [random.randint(1, 10000) for i in range(50)]
    print(sequence)
    print(bucket_sort(sequence))
