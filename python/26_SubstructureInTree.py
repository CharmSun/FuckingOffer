# 题目：树的子结构
# 输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
# B是A的子结构， 即 A中有出现和B相同的结构和节点值。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, treeA: TreeNode, treeB: TreeNode) -> bool:
        result = False
        if treeA and treeB:
            result = self.tree1HaveTree2(treeA, treeB)
            if result:
                return True
            else:
                result= self.isSubStructure(treeA.left, treeB) or \
                        self.isSubStructure(treeA.right, treeB)
        return result

    def tree1HaveTree2(self, tree1: TreeNode, tree2: TreeNode) -> bool:
        if not tree2:
            return True
        if not tree1:
            return False
        if tree1.val != tree2.val:
            return False
        return self.tree1HaveTree2(tree1.left, tree2.left) and \
                self.tree1HaveTree2(tree1.right, tree2.right)
