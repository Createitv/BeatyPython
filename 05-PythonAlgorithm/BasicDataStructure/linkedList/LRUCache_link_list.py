#!/Users/tnt/Documents/虚拟环境/Py4E/bin/python3
# -*- encoding: utf-8 -*-
# Time  : 2021/07/12 22:28:33
# Theme : LRU链表缓存算法
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


class ListNode():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LRUCache():
    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = ListNode(None, None)
        self.length = 0

    def __len__(self):
        return self.length

    def get(self, val: object) -> bool:
        prev = None  # 用于记录尾节点的前一个节点
        p = self.head
        # 如果此数据之前已经被缓存在链表中了
        while p.next:
            if p.next.val == val:
                # 将目标节点从原来的位置删除
                dest = p.next  # dest临时保存目标节点
                p.next = dest.next
                # 将目标节点插入到头部
                self.insert_to_head(self.head, dest)
                return True
            prev = p
            p = p.next

        # 如果此数据没有缓存在链表中
        self.insert_to_head(self.head, ListNode(val))
        self.length += 1
        # 添加数据导致超过容量则要删除尾节点
        if self.length > self.cap:
            prev.next = None
        return False

    @staticmethod
    def insert_to_head(head, node):
        """将指定节点插入到头部"""
        node.next = head.next
        head.next = node

    def __repr__(self):
        vals = []
        p = self.head.next
        while p:
            vals.append(str(p.val))
            p = p.next
        return '->'.join(vals)


if __name__ == '__main__':
    cache = LRUCache(4)
    for n in range(40):
        i = random.randint(0, 7)
        print("cache.get(%d)" % i, cache.get(i), cache)
