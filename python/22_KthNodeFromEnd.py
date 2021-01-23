# 题目：链表中倒数第K个节点
# 输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，
# 本题从1开始计数，即链表的尾节点是倒数第1个节点。
# 例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。
# 这个链表的倒数第3个节点是值为4的节点。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if not head or k <= 0:
            return None
        i = 0
        p = head
        res = None
        while p:
            p = p.next
            i += 1
            if i == k:
                res = head
            if i > k:
                res = res.next
        return res
