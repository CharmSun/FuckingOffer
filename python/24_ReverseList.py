# 题目： 反转链表
# 定义一个函数，输入一个链表的头节点，反转该链表并输出
# 反转后链表的头节点。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            nextNode = cur.next
            cur.next = pre
            pre = cur
            cur = nextNode
        return pre