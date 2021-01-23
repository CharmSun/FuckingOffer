# 题目：二叉树中和为某一值的路径
# 输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。
# 从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import List

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        self.dfs(root, sum, 0, [], res)
        return res

    def dfs(self, root: TreeNode, sum: int, cur: int, path: List[int], res):
        if not root:
            return
        cur += root.val
        path.append(root.val)
        if not root.left and not root.right:
            if cur == sum:
                res.append(path.copy())
        self.dfs(root.left, sum, cur, path, res)
        self.dfs(root.right, sum, cur, path, res)
        path.pop()