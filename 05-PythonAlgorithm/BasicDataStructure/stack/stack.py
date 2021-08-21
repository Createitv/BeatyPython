class Stack(object):
    """
    栈允许进行插入和删除操作的一端称为栈顶(top)，另一端为栈底(bottom)；
    栈底固定，而栈顶浮动；栈中元素个数为零时称为空栈。插入一般称为进栈（PUSH），
    删除则称为退栈（POP)
    """

    def __init__(self, limit=20):
        self.stack = []  # 存放元素
        self.limit = limit  # 栈容量极限

    def push(self, data):
        # 判断栈是否溢出
        if len(self.stack) >= self.limit:
            raise IndexError('超出栈容量极限')
        self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            # 空栈不能被弹出元素
            raise IndexError('pop from an empty stack')

    def peek(self):
        # 查看栈的栈顶元素（最上面的元素）
        if self.stack:
            return self.stack[-1]

    def is_empty(self):
        # 查看堆栈的最上面的元素
        return not bool(self.stack)  # 判断栈是否溢

    def size(self):
        # 返回栈的大小
        return len(self.stack)

    def __str__(self):
        # 返回整个栈
        return str(self.stack)
