# 题目：删除链表的节点
# 在O(1)时间内删除链表节点

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    # 确保要删除的节点在链表中
    def deleteNode(self, head: ListNode, toBeDeleted: ListNode):
        if not head or not toBeDeleted:
            return
        # 要删除的节点不是尾结点，复制下一个节点，删除下一个节点
        if toBeDeleted.next:
            toBeDeleted.val = toBeDeleted.next.val
            toBeDeleted.next = toBeDeleted.next.next
        # 链表只有一个节点时
        elif head == toBeDeleted:
            head = None
        # 要删除的节点是尾节点
        else:
            p = head
            while p.next != toBeDeleted:
                p = p.next
            p.next = None