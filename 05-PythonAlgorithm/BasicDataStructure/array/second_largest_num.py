#!/Users/tnt/Documents/虚拟环境/Py4E/bin/python3
# -*- encoding: utf-8 -*-
# Time  : 2021/07/25 22:41:43
# Theme : 寻找数组中第二个最大元素
def find_second_maximum_1(lst):
    first_max = float('-inf')
    second_max = float('-inf')
    # find first max
    for item in lst:
        if item > first_max:
            first_max = item
    # find max relative to first max
    for item in lst:
        if item != first_max and item > second_max:
            second_max = item
    return second_max


def find_second_maximum(lst):
    """initialize two variables max_no and secondmax to -inf. We then traverse the list, and if the current element in the list is greater than the maximum value, then set secondmax to max_no and max_no to the current element. If the current element is greater than the second maximum number and not equal to maximum number, then update secondmax to store the value of the current variable. Finally, return the value stored in secondmax."""
    if (len(lst) < 2):
        return
    # initialize the two to infinity
    max_no = second_max_no = float('-inf')
    for i in range(len(lst)):
        # update the max_no if max_no value found
        if (lst[i] > max_no):
            second_max_no = max_no
            max_no = lst[i]
        # check if it is the second_max_no and not equal to max_no
        elif (lst[i] > second_max_no and lst[i] != max_no):
            second_max_no = lst[i]
    if (second_max_no == float('-inf')):
        return
    else:
        return second_max_no


print(find_second_maximum([9, 2, 3, 6]))
print(find_second_maximum([9, 2, 3, 6]))
