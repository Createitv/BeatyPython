#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Time  : 2021/05/25 10:22:12
# Theme : pythonic版本,用字典匹配双括号
from stack import Stack


def match_symbols(symbol_str):

    symbol_pairs = {
        '(': ')',
        '[': ']',
        '{': '}',
    }

    openers = symbol_pairs.keys()
    my_stack = Stack()

    index = 0
    while index < len(symbol_str):
        symbol = symbol_str[index]

        if symbol in openers:
            my_stack.push(symbol)
        else:  # The symbol is a closer

            # If the Stack is already empty, the symbols are not balanced
            if my_stack.is_empty():
                return False

            # If there are still items in the Stack, check for a mis-match.
            else:
                top_item = my_stack.pop()
                if symbol != symbol_pairs[top_item]:
                    return False

        index += 1

    if my_stack.is_empty():
        return True

    return False  # Stack is not empty so symbols were not balanced


print(match_symbols('([{}])'))
print(match_symbols('(([{}]])'))

# 简单写法
"""
提前返回优点： 在迭代过程中，提前发现不符合的括号并且返回，提升算法效率。
解决边界问题：
栈 stack 为空： 此时 stack.pop() 操作会报错；因此，我们采用一个取巧方法，给 stack 赋初值 ?? ，并在哈希表 dic 中建立 key: '?'，value:'?',
  的对应关系予以配合。此时当 stack 为空且 c 为右括号时，可以正常提前返回 falsefalse；
字符串 s 以左括号结尾： 此情况下可以正常遍历完整个 s，但 stack 中遗留未出栈的左括号；因此，最后需返回 len(stack) == 1，以判断是否是有效的括号组合。
"""


def isValid(self, s: str) -> bool:
    dic = {'{': '}', '[': ']', '(': ')', '?': '?'}
    stack = ['?']
    for c in s:
        if c in dic:
            stack.append(c)
        elif dic[stack.pop()] != c:
            return False
    return len(stack) == 1
