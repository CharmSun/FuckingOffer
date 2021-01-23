# 题目： 合并两个排序的链表
# 输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l2:
            return l1
        if not l1:
            return l2
        p, q = l1, l2
        dummy = k = ListNode(0)
        while p and q:
            if p.val <= q.val:
                k.next = p
                p = p.next
            else:
                k.next = q
                q = q.next
            k = k.next
        if p:
            k.next = p
        elif q:
            k.next = q
        return dummy.next