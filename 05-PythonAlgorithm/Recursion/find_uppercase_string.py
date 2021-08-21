#!/Users/tnt/Documents/虚拟环境/Django/bin/python3
# -*- encoding: utf-8 -*-
# Time  : 2021/05/25 18:37:50
# Theme : Find Uppercase Letter in String


# Iterative Approach 
def find_uppercase_iterative(input_str):
    for i in range(0, len(input_str)):
        if input_str[i].isupper():
            return input_str[i]
        return "No uppercase character found"

# Recursive Approach 
def find_uppercase_recursive(input_str, index=0):
    if input_str[index].isupper():
        return input_str[index]
    if index == len(input_str) - 1:
        return "No uppercase character found"
    return find_uppercase_recursive(input_str, index + 1)

# Recursive print_list
def print_list(num, index=0):
    if index < num:
        print(index)
    if index == num-1:
        return ''
    return print_list(num, index+1)

print_list(10)
input_str_1 = "lucidProgramming"
input_str_2 = "LucidProgramming"
input_str_3 = "lucidprogramming"

print(find_uppercase_iterative(input_str_1))
print(find_uppercase_iterative(input_str_2))
print(find_uppercase_iterative(input_str_3))

print(find_uppercase_recursive(input_str_1))
print(find_uppercase_recursive(input_str_2))
print(find_uppercase_recursive(input_str_3))