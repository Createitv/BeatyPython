#!/Users/tnt/Documents/虚拟环境/Django/bin/python3
# -*- encoding: utf-8 -*-
# Time  : 2021/05/25 20:19:23
# Theme : fibonacc

def fibonacc(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacc(n - 1) + fibonacc(n - 2)


for i in range(1, 10):
    print(fibonacc(i), end=' ')
