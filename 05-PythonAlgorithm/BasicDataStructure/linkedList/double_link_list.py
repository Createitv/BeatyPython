class Node():
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoubleLinkedList(Node):
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            # 链尾指向新的链尾，链尾头节点指向原来的链尾
            cur.next = new_node
            new_node.pre = cur

    def prepend(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            # 创建新节点
            new_node = Node(data)
            # 旧头pre指针指向新节点
            self.head.pre = new_node
            # 新节点的尾指针指向头
            new_node.next = self.head
            # 初始化头节点，指向新加入的节点，为下一个后加入的元素备头
            self.head = new_node

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def add_after_node(self, key, data):
        cur = self.head
        while cur:
            if cur.next is None and cur.data == key:
                self.append(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                nxt = cur.next
                cur.next = new_node
                new_node.next = nxt
                new_node.pre = cur
                nxt.prev = new_node
                return
            cur = cur.next

    def reverse(self):
        tmp = None
        cur = self.head
        while cur:
            tmp = cur.prev
            cur.prev = cur.next
            cur.next = tmp
            cur = cur.prev
        if tmp:
            self.head = tmp.pre


if __name__ == "__main__":
    dllist = DoubleLinkedList()
    dllist.prepend(0)
    dllist.append(1)
    dllist.append(2)
    dllist.append(3)
    dllist.append(4)
    dllist.prepend(5)

    dllist.print_list()
