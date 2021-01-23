# 题目：二叉搜索树的后序遍历序列
# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是
# 则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。
from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if not postorder:
            return True
        root = postorder[-1]
        i = 0
        while i < len(postorder) - 1 and postorder[i] < root:
            i += 1
        j = i
        while j < len(postorder) - 1:
            if postorder[j] < root:
                return False
            j += 1
        if i > 0 and not self.verifyPostorder(postorder[0:i]):
            return False
        if i < len(postorder) - 1 and not self.verifyPostorder(postorder[i:-1]):
            return False
        return True
