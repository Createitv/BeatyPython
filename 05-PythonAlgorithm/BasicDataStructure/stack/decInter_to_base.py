#!/Users/tnt/Documents/虚拟环境/Py4E/bin/python3
# -*- encoding: utf-8 -*-
# Time  : 2021/07/16 18:25:02
# Theme : 10进制转任意进制

from stack import Stack


def convertDecToBase(num, base):
    stack = Stack()
    while num != 0:
        remainer, num = num % base, num // base
        stack.push(str(remainer))

    string = ''
    for _ in range(stack.size()):
        string += stack.pop()
    return string


print(convertDecToBase(100, 2))
