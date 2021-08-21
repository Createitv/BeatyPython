#!/Users/tnt/Documents/虚拟环境/Py4E/bin/python3
# -*- encoding: utf-8 -*-
# Time  : 2021/07/25 16:23:59
# Theme : 两个排序好的数组求交集

# A = [2, 3, 3, 5, 7, 11]
# B = [3, 3, 7, 15, 31]
# print(set(A).intersection(B))


def intersect_sorted_array(A, B):
    """
    双指针移动轮训数组求交集
    """
    i = 0
    j = 0
    intersection = []

    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if i == 0 or A[i] != A[i - 1]:
                intersection.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    return intersection


A = [2, 3, 3, 5, 7, 11]
B = [3, 3, 7, 15, 31]

print(intersect_sorted_array(A, B))
