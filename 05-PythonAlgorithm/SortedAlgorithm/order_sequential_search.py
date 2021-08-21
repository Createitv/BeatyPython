#!/usr/local/bin python
# -*- encoding: utf-8 -*-
# Time  : 2021/05/12 13:19:38
# Theme : 有序列表查询
# 假定数据集合已经按大小顺序排序好了

def orderedSequentialSearch(alsit, item):
    pos = 0
    found = False
    stop = False
    while pos < len(alsit) and not found and not stop:
        if alsit[pos] == item:
            found = True
        else:
            if alsit[pos] > item:
                stop = True
            else:
                pos += 1
    return found


test_lst = [1, 2, 3, 4, 23, 35, 54, 73, 3121]
print(orderedSequentialSearch(test_lst, 23))
