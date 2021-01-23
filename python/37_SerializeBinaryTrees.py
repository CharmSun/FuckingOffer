# 题目：序列化二叉树
# 请实现两个函数，分别用来序列化和反序列化二叉树。

from collections import deque

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '[]'
        queue = deque([root])
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append('null')
        while res[-1] == 'null':
            res.pop()
        return '['+','.join(res)+']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '[]':
            return None
        vals = data[1:-1].split(',')
        n = len(vals)
        root = TreeNode(int(vals[0]))
        queue = deque([root])
        i = 0
        while i < n:
            i += 1
            if i >= n:
                return root
            node = queue.popleft()
            if vals[i] != 'null':
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if i >= n:
                return root
            if vals[i] != 'null':
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)


s = "[1,2,3,null,null,4,5]"
codec = Codec()
print(codec.serialize(codec.deserialize(s)))
