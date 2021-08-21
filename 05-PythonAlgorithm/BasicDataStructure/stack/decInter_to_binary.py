#!/Users/tnt/Documents/虚拟环境/Django/bin/python3
# -*- encoding: utf-8 -*-
# Time  : 2021/05/25 11:28:57
# Theme : Convert Decimal Integer to Binary

from stack import Stack


def convertDecToBinary(stack, num):
    while num != 0:
        remainer, num = num % 2, num // 2
        stack.push(str(remainer))
    string = ""
    for i in range(stack.size()):
        string += stack.pop()
    return int(string)


stack = Stack()
print(convertDecToBinary(stack, 33))
print(convertDecToBinary(stack, 44))
