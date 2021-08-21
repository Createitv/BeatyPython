#!/Users/tnt/Documents/虚拟环境/Py4E/bin/python3
# -*- encoding: utf-8 -*-
# Time  : 2021/07/25 21:10:37
# Theme : 列表两数字相加等于k
# 先排序，前后双指针相加比大小移动前后指针 复杂度：nlog(n)

def find_sum_0(lst, k):
    # Write your code here
    for i in lst:
        if k - i in lst and k - i != i:
            return [i, k - i]
    return False


def find_sum(lst, k):
    # sort the list
    lst.sort()
    index1 = 0
    index2 = len(lst) - 1
    result = []
    sum = 0
    # iterate from front and back
    # move accordingly to reach the sum to be equal to k
    # returns false when the two indices meet
    while (index1 != index2):
        sum = lst[index1] + lst[index2]
        if sum < k:
            index1 += 1
        elif sum > k:
            index2 -= 1
        else:
            result.append(lst[index1])
            result.append(lst[index2])
            return result
    return False


print(find_sum([1, 2, 3, 4], 5))
print(find_sum_0([1, 2, 3, 4], 2))
