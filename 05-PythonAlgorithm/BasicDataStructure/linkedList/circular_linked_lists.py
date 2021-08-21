#!/Users/tnt/Documents/虚拟环境/Django/bin/python3
# -*- encoding: utf-8 -*-
# Time  : 2021/05/27 08:04:03
# Theme : 循环链表

class Node():
    def __init__(self, data):
        self.data = data
        self.next = next
    
class CircularLinkedList():
    def __init__(self):
        self.head = None
    
    def append(self,data):
        #头节点为空尾指针指向自己
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            cur = self.head
    # 循环当前节点不等于头节点地址就一直往后，等于就相当于找到了尾节点
            while cur.next != self.head:
                cur = cur.next
    # 将尾巴节点指向新加入节点地址，再将新节点地址指向头节点
            cur.next =new_node
            new_node.next = self.head
    
    def print_list(self):
        cur =self.head
        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break
    
    def prepend(self, data):
        new_node = Node(data)
        cur = self.head
        # 新节点地址指向头节点
        new_node.next = cur
        # 为空则指向自己
        if not self.head:
            new_node.next = new_node
        else:
            # 尾节点指向头地址
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
        # 链头移到新节点
        self.head = new_node
    
    def remove(self, key):
        if self.head:
            if self.head.data == key:
                cur = self.head
                while cur.next != self.head:
                    cur = cur.next
                # 如果刚好只有一个元素
                if self.head == self.head.next:
                    self.head = None
                else:
                    # 尾节点指向头节点下一节点地址
                    cur.next = self.head.next
                    # 头节点移动到头节点下一节点地址
                    self.head = self.head.next
            else:
                cur =  self.head
                prev = None
                while cur.next != self.head:
                    prev = cur
                    cur = cur.next
                    if cur.data  == key:
                        prev.next = cur.next
                        cur = cur.next
        else:
            raise IndexError("List is None")
    
    def __len__(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
            if cur == self.head:
                break
        return count
    
    def split_list(self):
        size = len(self)
        if size == 0:
            return None
        if size == 1:
            return self.head
        mid = size // 2
        count = 0
        prev = None
        cur  = self.head
        while cur and count < mid:
            count += 1
            prev = cur
            cur = cur.next
        prev.next = self.head
        
        split_cllist = CircularLinkedList()
        while cur.next != self.head:
            split_cllist.append(cur.data)
            cur = cur.next
        split_cllist.append(cur.data)

        self.print_list()
        print("\n")
        split_cllist.print_list()

    def remove_node(self, node):
        if slef.head == node:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            if self.head == self.head.next:
                self.head = None
            else:
                cur.next = self.head.next
                self.head = self.head.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur == node:
                    prev.next = cur.next
                    cur = cur.next

    def josephus_circle(self, step):
        cur = self.head
        length = len(self)
        while length > 1:
            count = 1
            while count != step:
                cur = cur.next
                count += 1
            print("KIll" + str(cur.data))
            self.remove_node(cur)
            cur = cur.next
            length -= 1
            
    def is_circular_linked_list(self, input_list):
        if input_list.head:
            cur = input_list.head
            while cur.next:
                cur = cur.next
                if cur.next == input_list.head:
                    return True
            return False
        else:
            return False
    
cllist = CircularLinkedList()
cllist.append(1)
# cllist.append(2)
# # cllist.append(3)
# # cllist.append(4)
from single_link_list import LinkedList
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)

print(cllist.is_circular_linked_list(cllist))
print(cllist.is_circular_linked_list(llist))