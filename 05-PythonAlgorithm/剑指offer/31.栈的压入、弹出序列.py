class Solution:
    """解题思路
    1.定义一个栈stack作为模拟栈
    2.遍历pushed数组的同时将pushed中的元素压入stack模拟压栈过程
    3.判断stack的栈顶元素是否与popped数组中的第i个元素相同，相同则弹出stack
    4.最后判断stack是否弹空，弹空则返回true，不空则为false
    """
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack, i = [], 0
        for num in pushed:
            stack.append(num)  # num 入栈
            while stack and stack[-1] == popped[i]:  # 循环判断与出栈
                stack.pop()
                i += 1
        return not stack
