#!/Users/tnt/Documents/虚拟环境/Py4E/bin/python3
# -*- encoding: utf-8 -*-
# Time  : 2021/07/12 22:28:33
# Theme : LRU哈希s双链表缓存算法
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
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        # 新建两个节点 head 和 tail 哨兵节点
        self.head = ListNode()
        self.tail = ListNode()
        # 初始化链表为 head <-> tail
        self.head.next = self.tail
        self.tail.prev = self.head

    # 因为get与put操作都可能需要将双向链表中的某个节点移到头部(变成最新访问的)，所以定义一个方法
    def move_node_to_header(self, key):
        # 先将哈希表key指向的节点拎出来，为了简洁起名node
        #      hashmap[key]                               hashmap[key]
        #           |                                          |
        #           V              -->                         V
        # prev <-> node <-> next         pre <-> next   ...   node
        node = self.hashmap[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        # 之后将node插入到头部节点前
        #                   hashmap[key]                     hashmap[key]
        #                       |                                 |
        #                       V        -->                      V
        # header <-> next  ... node                   header <-> node <-> next
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def add_node_to_header(self, key, value):
        new = ListNode(key, value)
        self.hashmap[key] = new
        new.prev = self.head
        new.next = self.head.next
        self.head.next.prev = new
        self.head.next = new

    def pop_tail(self):
        last_node = self.tail.prev
        # 去掉链表尾部的节点在哈希表的对应项
        self.hashmap.pop(last_node.key)
        # 去掉最久没有被访问过的节点，即尾部Tail之前的一个节点
        last_node.prev.next = self.tail
        self.tail.prev = last_node.prev
        return last_node

    def get(self, key: int) -> int:
        if key in self.hashmap:
            # 如果已经在链表中了久把它移到头部（变成最新访问的）
            self.move_node_to_header(key)
        res = self.hashmap.get(key, -1)
        if res == -1:
            return res
        else:
            return res.value

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            # 如果key本身已经在哈希表中了就不需要在链表中加入新的节点
            # 但是需要更新字典该值对应节点的value
            self.hashmap[key].value = value
            # 之后将该节点移到链表头部
            self.move_node_to_header(key)
        else:
            if len(self.hashmap) >= self.capacity:
                # 若cache容量已满，删除cache中最不常用的节点
                self.pop_tail()
            self.add_node_to_header(key, value)
