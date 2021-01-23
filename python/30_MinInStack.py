# 题目： 包含 min 函数的栈
# 定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的
# min 函数。在该栈中，调用min、push 及pop 的时间复杂度都是 O(1)

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min_stack = []


    def push(self, x: int) -> None:
        self.data.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> None:
        if not self.data:
            raise Exception('stack is empty')
        x = self.data.pop()
        if x == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        if not self.data:
            raise Exception('stack is empty')
        return self.data[-1]

    def min(self) -> int:
        if not self.min_stack:
            raise Exception('stack is empty')
        return self.min_stack[-1]