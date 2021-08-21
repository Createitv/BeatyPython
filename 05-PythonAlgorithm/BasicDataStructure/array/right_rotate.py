#!/Users/tnt/Documents/虚拟环境/Py4E/bin/python3
# -*- encoding: utf-8 -*-
# Time  : 2021/07/25 22:58:47
# Theme : 右旋转

def right_rotate(lst, k):
    """
    最右侧几个元素放到头
    >>> right_rotate([1, 2, 3, 4, 5], 2)
    [4, 5, 1, 2, 3]
    >>> right_rotate([300, -1, 3, 0], 3)
    [-1, 3, 0, 300]
    """
    # get rotation index
    if len(lst) == 0:
        k = 0
    else:
        k = k % len(lst)
    return lst[-k:] + lst[:-k]


print(right_rotate([10, 20, 30, 40, 50], abs(3)))
