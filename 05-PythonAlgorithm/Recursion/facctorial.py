#!/Users/tnt/Documents/虚拟环境/Django/bin/python3
# -*- encoding: utf-8 -*-
# Time  : 2021/05/25 21:01:39
# Theme : stack循环实现阶乘，凡事能用递归实现的都必能用循环和stack实现


# Using iteration to emulate recursive
callStack = []
callStack.append({'instrPtr': 'start', 'number': 5})
returnValue = None

while len(callStack) > 0:
    number = callStack[-1]['number']
    instrPtr = callStack[-1]['instrPtr']

    if instrPtr == "start":
        if number == 1:
            returnValue = 1
            callStack.pop()
            continue
        else:
            callStack[-1]['instrPtr'] = "after recursive call"
            callStack.append({'instrPtr': 'start', 'number': number - 1})
            continue
    elif instrPtr == "after recursive call":
        returnValue = number * returnValue
        callStack.pop()
        continue

print(returnValue)
