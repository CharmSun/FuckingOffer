# 题目：二叉搜索树的第K大节点
# 给定一棵二叉搜索树，请找出其中第k大的节点。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 注意是第k大的数，按右中左的顺序遍历
    def kthLargest(self, root: TreeNode, k: int) -> int:
        stack = []
        p = root
        i = 0
        while stack or p:
            while p:
                stack.append(p)
                p = p.right
            node = stack.pop()
            i += 1
            if i == k:
                return node.val
            p = node.left
        return None