# !/usr/bin/env python
# -*- encoding: utf-8 -*-
# Time  : 2021/04/28 10:38:23
# Theme : 希尔排序
# 复杂度分析
# 最坏复杂度: 时间复杂度为 O(n(logn) ^ 2)
# 最好复杂度：时间复杂度为 O(nlogn)
# 平均复杂度: 取决于间隔序列

def shell_sort(sequence):
    gap = len(sequence)
    while gap > 1:
        gap = gap//2
        for i in range(gap, len(sequence)):
            for j in range(i % gap, i, gap):
                if sequence[i] < sequence[j]:
                    sequence[i], sequence[j] = sequence[j], sequence[i]
    return sequence
