# 题目：队列的最大值
# 请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back
# 和 pop_front 的均摊时间复杂度都是O(1)。
# 若队列为空，pop_front 和 max_value 需要返回 -1
from collections import deque


class MaxQueue:

    def __init__(self):
        self.queue = deque([])
        self.maxQ = deque([])

    def max_value(self) -> int:
        if not self.maxQ:
            return -1
        return self.maxQ[0]

    def push_back(self, value: int) -> None:
        while self.maxQ and value > self.maxQ[-1]:
            self.maxQ.pop()
        self.queue.append(value)
        self.maxQ.append(value)

    def pop_front(self) -> int:
        if not self.queue:
            return -1
        val = self.queue.popleft()
        if val == self.maxQ[0]:
            self.maxQ.popleft()
        return val
