# 题目：栈的压入、弹出序列
# 输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个
# 序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。
# 例如，序列{1,2,3,4,5}是某栈的压栈序列，序列{4,5,3,2,1}是该压栈序列
# 对应的一个弹出序列，但{4,3,5,1,2}就不可能是该压栈序列的弹出序列。
from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if not pushed and not popped:
            return True
        if not pushed or not popped:
            return False
        res = False
        i, j = 0, 0
        stack = []
        while j < len(popped):
            while i < len(pushed) \
                and (len(stack) == 0 or stack[-1] != popped[j]):
                stack.append(pushed[i])
                i += 1
            if stack[-1] != popped[j]:
                break
            stack.pop()
            j += 1
        if j == len(popped) and not stack:
            res = True
        return res