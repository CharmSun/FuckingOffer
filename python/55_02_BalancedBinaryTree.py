# 题目：平衡二叉树
# 输入一棵二叉树的根节点，判断该树是不是平衡二叉树。
# 如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.calBHeight(root) != -1

    # 后序遍历：计算平衡树的高度，不平衡返回-1，平衡则返回树的高度
    def calBHeight(self, root) -> int:
        if not root:
            return 0
        leftH = self.calBHeight(root.left)
        if leftH == -1:
            return -1
        rightH = self.calBHeight(root.right)
        if rightH == -1:
            return -1
        if abs(leftH - rightH) > 1:
            return -1
        return max(leftH, rightH) + 1
