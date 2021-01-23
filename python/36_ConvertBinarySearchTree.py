# 题目：二叉搜索树与双向链表
# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。
# 要求不能创建任何新的节点，只能调整树中节点指针的指向。

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def __init__(self) -> None:
        self.lastInList = None
        self.head = None

    # 中序遍历，递归
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        self.convert(root)
        self.head.left = self.lastInList
        self.lastInList.right = self.head
        return self.head

    def convert(self, root):
        if not root:
            return
        current = root
        if current.left:
            self.convert(current.left)
        current.left = self.lastInList
        if self.lastInList:
            self.lastInList.right = current
        else:
            self.head = current
        self.lastInList = current
        if current.right:
            self.convert(current.right)

    
    # 中序遍历，栈
    def treeToDoublyList1(self, root: 'Node') -> 'Node':
        if not root:
            return None
        p = root
        head = last = None
        stack = []
        while p or stack:
            if p:
                stack.append(p)
                p = p.left
            else:
                node = stack.pop()
                if last:
                    last.right = node
                    node.left = last
                else:
                    head = node
                last = node
                p = node.right
        head.left = last
        last.right = head
        return head
