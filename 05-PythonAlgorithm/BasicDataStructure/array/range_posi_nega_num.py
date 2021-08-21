#!/Users/tnt/Documents/虚拟环境/Py4E/bin/python3
# -*- encoding: utf-8 -*-
# Time  : 2021/07/25 23:15:32
# Theme : 重新安排列表中正负数的位置

def rearrange(lst):
    # get negative and positive list after filter and then merge
    """
    >>> rearrange([-1, 2, -3, -4, 5])
    [-1, -3, -4, 2, 5]
    >>> rearrange([300, -1, 3, 0])
    [-1, 300, 3, 0]
    >>> rearrange([0, 0, 0, -2])
    [-2, 0, 0, 0]
    """

    return [i for i in lst if i < 0] + [i for i in lst if i >= 0]


# print(rearrange([10, -1, 20, 4, 5, -9, -6]))
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
