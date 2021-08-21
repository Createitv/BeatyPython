# !/usr/bin/env python
# -*- encoding: utf-8 -*-
# Time  : 2021/04/28 10:31:10
# Theme : 插入排序
'''
❖ 第1趟，子列表仅包含第1个数据项，将第 2个数据项作为“新项”插入到子列表的 合适位置中，这样已排序的子列表就包含 了2个数据项
❖ 第2趟，再继续将第3个数据项跟前2个数 据项比对，并移动比自身大的数据项，空 出位置来，以便加入到子列表中
❖ 经过n-1趟比对和插入，子列表扩展到全 表，排序完成
'''
# 复杂度分析
# 最坏复杂度: 时间复杂度为 O(n ^ 2)
# 最好复杂度：时间复杂度为 O(n ^ 2)
# 平均复杂度: 时间复杂度为 O(n ^ 2)
def insertion_sort(sequence):
    for index in range(1, len(sequence)):
        while(index > 0 and sequence[index-1] > sequence[index]):
            sequence[index], sequence[index -
                                      1] = sequence[index-1], sequence[index]
            index = index - 1
    return sequence

