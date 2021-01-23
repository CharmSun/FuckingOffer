# 题目：重建二叉树
# 输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。
# 假设输入的前序遍历和中序遍历的结果中都不包含重复的数字。

from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        if len(preorder) != len(inorder):
            return None
        root = TreeNode(preorder[0])
        i = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:1+i], inorder[0:i])
        root.right = self.buildTree(preorder[1+i:], inorder[1+i:])

        return root
