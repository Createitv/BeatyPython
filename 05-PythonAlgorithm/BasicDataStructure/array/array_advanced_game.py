#!/Users/tnt/Documents/虚拟环境/Django/bin/python3
# -*- encoding: utf-8 -*-
# Time  : 2021/05/27 10:48:33
# Theme : https://www.educative.io/module/lesson/data-structures-algorithms-in-python/xoPKRnVpp5l

def array_advance(A):
    
    furthest_reached = 0
    last_idx = len(A) - 1
    i = 0
    while i <= furthest_reached and furthest_reached < last_idx:
        furthest_reached  = max(furthest_reached, A[i] + i)
        i += 1
    return furthest_reached >= last_idx

print(array_advance([3,3,1,0,2,0,1]))
