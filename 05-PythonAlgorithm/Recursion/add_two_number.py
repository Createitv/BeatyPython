#!/Users/tnt/Documents/虚拟环境/Django/bin/python3
# -*- encoding: utf-8 -*-
# Time  : 2021/05/25 20:16:48
# Theme : 两数相加
def recursive_multiply(x, y):
    if x < y:
        return recursive_multiply(y, x)
    if y == 0:
        return 0
    return x + recursive_multiply(x, y - 1)
print(recursive_multiply(3,4))