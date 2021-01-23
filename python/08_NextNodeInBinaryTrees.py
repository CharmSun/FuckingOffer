# 题目： 二叉树的下一个节点
# 给定一颗二叉树和其中的一个节点，如何找出中序遍历序列的
# 下一个节点？树中的节点除了有两个分别指向左、右子节点的指针，
# 还有一个指向父节点的指针。

# class TreeLinkNode:
#     def __init__(self, val=0, left=None, right=None, parent=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.parent = parent

class Solution:

    # 如果一个节点有右子树，下一个节点就是它右子树的最左子节点。
    # 如果一个节点没有右子树，沿着父节点指针向上遍历，直到找到
    # 一个是它父节点左子节点的节点
    def getNext(self, pNode: TreeLinkNode) -> TreeLinkNode:
        if not pNode:
            return None
        if pNode.right:
            node = pNode.right
            while node.left:
                node = node.left
            return node
        elif pNode.parent:
            cur = pNode
            par = pNode.parent
            while par and cur == par.right:
                cur = par
                par = par.parent
            return par
        return None
