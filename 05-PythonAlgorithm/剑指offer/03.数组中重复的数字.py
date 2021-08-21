#!/Users/tnt/Documents/虚拟环境/Py4E/bin/python3
# -*- encoding: utf-8 -*-
# Time  : 2021/07/28 17:04:44
# Theme : 
# 链接：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        hashtable = {}
        for i in nums:
            if i not in hashtable:
                hashtable[i] = 1
            else:
                return i
        return -1