#!/Users/tnt/Documents/虚拟环境/Py4E/bin/python3
# -*- encoding: utf-8 -*-
# Time  : 2021/07/12 22:28:33
# Theme : LRU数组缓存算法
"""
缓存的大小是有限的,那些数据应该备清除，那些数据应该备保留，这就引入了缓存的淘汰策略
常见的三种策略：
- 1： FIFO先进先出
- 2:  LFU最少使用策略
- 3:  最近最少使用策略LRU(least Recently Used)

解决思路：
1.维护一个有序单链表，越靠近尾部的节点是越早之前访问的，一个新的缓存数据进来从头遍历，判断是否
已经在缓存种。
2.如果已经在缓存中，从原来位置删除，加入到表头
3.如果不在缓存中且缓存未满，直接插入到表头；如果不在缓存中且缓存满，删除尾节点再插入到表头。
"""
import random


class LRUCache(object):
    def __init__(self, capacity: int = 10):
        self.capacity = capacity
        self._data = []

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return str(self._data)

    def get(self, val: object) -> bool:
        """
        获取指定缓存数据
        参数：
            val:要获取的数据
        返回：
            存在于缓存中，返回True，否则返回 False。
        """
        for i in range(len(self._data)):
            if self._data[i] == val:
                self._data.insert(0, self._data.pop(i))
                return True

        # 添加数据导致超过容量则要删除尾节点
        if len(self) >= self.capacity:
            self._data.pop()
        # 如果此数据没有缓存在链表中
        self._data.insert(0, val)
        return False


if __name__ == '__main__':
    cache = LRUCache()
    for n in range(40):
        i = random.randint(0, 7)
        print("cache.get(%d)" % i, cache.get(i), cache)