# 题目：二叉树的深度
# 输入一棵二叉树的根节点，求该树的深度。
# 从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        lDepth = self.maxDepth(root.left)
        rDepth = self.maxDepth(root.right)
        return max(lDepth, rDepth) + 1

