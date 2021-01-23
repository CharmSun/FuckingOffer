# 题目： 对称的二叉树
# 请实现一个函数，用来判断一棵二叉树是不是对称的。
# 如果一棵二叉树和它的镜像一样，那么它是对称的。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2:
            return True
        if (root1 and not root2) or (not root1 and root2):
            return False
        return root1.val == root2.val \
            and self.isMirror(root1.left, root2.right) \
            and self.isMirror(root1.right, root2.left)

class Solution2:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        q1 = []
        q2 = []
        q1.append(root.left)
        q2.append(root.right)

        while q1 and q2:
            node1 = q1.pop(0)
            node2 = q2.pop(0)
            if (not node1 and node2) or (node1 and not node2):
                return False
            if node1 and node2:
                if node1.val != node2.val:
                    return False
                q1.append(node1.left)
                q1.append(node1.right)
                q2.append(node2.right)
                q2.append(node2.left)
        return True