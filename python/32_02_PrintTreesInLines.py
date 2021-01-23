# 题目：分行从上到下打印二叉树
# 从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List
from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = deque([root])
        while len(queue) > 0:
            level = []
            level_len = len(queue)
            for i in range(level_len):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res
