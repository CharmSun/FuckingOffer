# 复杂链表的复制
# 请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，
# 每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针
# 指向链表中的任意节点或者 null。

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# 1、在每个节点后创建一个该节点的复制
# 2、设置复制节点的random
# 3、将链表分成两个


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        l1 = head
        while l1:
            l2 = Node(l1.val)
            l2.next = l1.next
            l1.next = l2
            l1 = l2.next
        l1 = head
        while l1:
            if l1.random:
                l1.next.random = l1.random.next
            l1 = l1.next.next
        l1 = head
        newHead = l1.next
        while l1:
            l2 = l1.next
            l1.next = l2.next
            if l2.next:
                l2.next = l2.next.next
            l1 = l1.next
        return newHead
