#!/Users/tnt/Documents/虚拟环境/Django/bin/python3
# -*- encoding: utf-8 -*-
# Time  : 2021/05/25 19:26:52
# Theme : Calculate String Length

# iterative Approach
def iterative_str_len(input_str):
    input_str_len = 0
    for _ in input_str:
        input_str_len += 1
    return input_str_len

# Recursive Approach
def recursive_str_len(input_str):
    if input_str == "":
        return 0
    return 1 + recursive_str_len(input_str[1:])

input_str = "LucidProgramming"

print(iterative_str_len(input_str))
print(recursive_str_len(input_str))