#!/Users/tnt/Documents/虚拟环境/Django/bin/python3
# -*- encoding: utf-8 -*-
# Time  : 2021/05/27 15:17:57
# Theme : 括号匹配成功返回"Success",错误返回在哪里错误了

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])
def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, char in enumerate(text, 1):
        if char in "([{":
            # Process opening bracket, write your code here
            # passP
            opening_brackets_stack.append(Bracket(char, i))

        if char in ")]}":
            # Process closing bracket, write your code here
            # pass
            if len(opening_brackets_stack) == 0:
                return i
            else:
                top = opening_brackets_stack.pop()
                if not are_matching(top.char, char):
                    return i
    if len(opening_brackets_stack) == 0:
        return "Success"
    else:
        return opening_brackets_stack[-1].position


def main():
    text = input()
    # []-->Success
    
    # text = "[][()("
    mismatch = find_mismatch(text)
    print(mismatch)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
