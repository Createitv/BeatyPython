"""
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。
示例:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        # 最小栈栈顶位置不断添加的小的值保证栈顶的值最小，保证min的操作为O(1)
        if not self.minStack or self.stack[-1] > x:
            self.minStack.append(x)

    def pop(self) -> None:
        # 判断self.stack.pop()的时候，stack已经去除了栈头元素，如果值等于minStack的值，minStack也要相应去除，不等则不用管。
        if self.stack.pop() == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(3)
obj.push(3)
obj.push(4)
obj.push(4)
obj.push(-1)
obj.push(67)
obj.pop()
param_3 = obj.top()
param_4 = obj.min()
print(param_3, param_4)
