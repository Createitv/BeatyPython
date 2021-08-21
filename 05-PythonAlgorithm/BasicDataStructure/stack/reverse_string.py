#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Time  : 2021/05/25 11:06:20
# Theme : Stack 字符串反转
"""
input_str = "Educative"
print(input_str[::-1])
"""

from stack import Stack


def str_reverse(string_match):
    "write first time"

    stack = Stack()
    index = 0
    while index < len(string_match):
        stack.push(string_match[index])
        index += 1

    count = 0
    string = ''
    size = stack.size()
    while count < size:
        string += stack.pop()
        count += 1

    return string


def reverse_string(stack, input_str):
    # 函数命名 动词+名词不要名次加动词
    # 函数里面不要创建对象，最好传入对象，避免空间浪费
    # 代码精简，过程太繁杂
    for i in range(len(input_str)):
        stack.push(input_str[i])
    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()
    return rev_str

# 第一次写法调用
# print(str_reverse("sdad"))  

# 第二次写法调用
stack = Stack(20)
print(reverse_string(stack,"!da2P aa;s;21"))