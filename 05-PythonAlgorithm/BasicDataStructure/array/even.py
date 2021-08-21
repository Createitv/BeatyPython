#!/Users/tnt/Documents/虚拟环境/Py4E/bin/python3
# -*- encoding: utf-8 -*-
# Time  : 2021/07/25 19:55:19
# Theme : 数组去除偶数

def remove_even(lst):
    return [item for item in lst if item % 2 != 0]


def remove_even(lst):
    # Write your code here!
    for i in sorted(lst):
        if i % 2 == 0:
            lst.remove(i)
    return lst


def remove_even(lst):
    # Write your code here!
    return list(filter(lambda x: x % 2 != 0, lst))
