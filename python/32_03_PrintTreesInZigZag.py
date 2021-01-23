# 题目：之字形打印二叉树
# 请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，
# 第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List
from collections import deque


class Solution:

    # 书上方法是轮流使用两个栈
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = deque([root])
        while len(queue) > 0:
            level_no = len(res)
            level_vals = []
            level_len = len(queue)
            for i in range(level_len):
                node = queue.popleft()
                if level_no % 2 == 0:
                    level_vals.append(node.val)
                else:
                    level_vals.insert(0, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level_vals)
        return res
