#!/Users/tnt/Documents/虚拟环境/Django/bin/python3
# -*- encoding: utf-8 -*-
# Time  : 2021/05/26 11:26:29
# Theme : 找寻一个元素的第一个比他大的值，如果没有返回-1
""" 
Element        NGE
   13      -->    -1
   7       -->     12
   6       -->     12
   12      -->     -1
"""
from stack import Stack
def find_next_great_num(arr):
   stack = Stack()
   for i in range(0, len(arr)):
      if i == len(arr) - 1:
         stack.push({arr[i]: -1})
      # stack.push(arr[i])
      for j in range(1+i, len(arr)):
         if arr[i] < arr[j]:
            stack.push({arr[i]:arr[j]})
            break
         else:
            stack.push({arr[i]: -1})
            break
   return stack
print(find_next_great_num([7,13,6,12]))
