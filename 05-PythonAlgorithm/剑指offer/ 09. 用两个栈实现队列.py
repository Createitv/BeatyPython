class CQueue:
    def __init__(self):
        self.A, self.B = [], []

    def appendTail(self, value: int) -> None:
        # 第一个栈只存
        self.A.append(value)

    def deleteHead(self) -> int:
        # 第二个栈倒叙弹出，后序变前序，第一个栈中先进的作为第二个栈的栈顶，即队头
        # 如果B中有元素，直接弹出
        if self.B:
            return self.B.pop()
        if not self.A:
            return -1
        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead(
