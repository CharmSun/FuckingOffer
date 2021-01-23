# 题目： 删除链表中重复的节点

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        while pre.next:
            cur = pre.next
            while cur.next and cur.next.val == cur.val:
                cur = cur.next
            if pre.next != cur:
                pre.next = cur.next
            else:
                pre = cur
        return dummy.next
        