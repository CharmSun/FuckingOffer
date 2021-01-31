# 题目一：二叉搜索树的最近公共祖先
# 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
# 最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）”

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import List


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        small = min(p.val, q.val)
        big = max(p.val, q.val)
        if root.val <= big and root.val >= small:
            return root
        elif root.val > big:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < small:
            return self.lowestCommonAncestor(root.right, p, q)
        return None

# 题目二： 二叉树的最近公共祖先
# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。


# 说明:
# 所有节点的值都是唯一的。
# p、q 为不同节点且均存在于给定的二叉树中。


class Solution1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        path1 = []
        self.getNodePath(root, p, path1)
        path2 = []
        self.getNodePath(root, q, path2)
        i, j = 0, 0
        lastCommonNode = None
        while i < len(path1) and j < len(path2) and path1[i] == path2[j]:
            lastCommonNode = path1[i]
            i += 1
            j += 1
        return lastCommonNode

    def getNodePath(self, root: 'TreeNode', node: 'TreeNode', path: List['TreeNode']):
        if not root:
            return False
        path.append(root)
        if root == node:
            return True
        elif self.getNodePath(root.left, node, path):
            return True
        elif self.getNodePath(root.right, node, path):
            return True
        path.pop()
        return False
