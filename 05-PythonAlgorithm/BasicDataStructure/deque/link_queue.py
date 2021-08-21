# !/usr/bin/env python
# -*- encoding: utf-8 -*-
# Time  : 2021/04/28 10:04:16
# Theme : 链表实现队列
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def print_list(self):  # 遍历链表，并将元素依次打印出来
        print("linked_list:")
        temp = self.head
        new_list = []
        while temp is not None:
            new_list.append(temp.data)
            temp = temp.next
        print(new_list)

    def insert(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def swapNodes(self, d1, d2):
        prevD1 = None
        prevD2 = None
        if d1 == d2:
            return
        else:
            D1 = self.head
            while D1 is not None and D1.data != d1:
                prevD1 = D1
                D1 = D1.next
            D2 = self.head
            while D2 is not None and D2.data != d2:
                prevD2 = D2
                D2 = D2.next
            if D1 is None and D2 is None:
                return
            if prevD1 is not None:
                prevD1.next = D2
            else:
                self.head = D2
            if prevD2 is not None:
                prevD2.next = D1
            else:
                self.head = D1
            temp = D1.next
            D1.next = D2.next
            D2.next = temp


if __name__ == '__main__':
    list = Linkedlist()
    list.insert(5)
    list.insert(4)
    list.insert(3)
    list.insert(2)
    list.insert(1)
    list.print_list()
    list.swapNodes(1, 4)
    print("After swapping")
    list.print_list()
