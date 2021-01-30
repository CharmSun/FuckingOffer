# 题目：两个链表的第一个公共节点
# 输入两个链表，找出它们的第一个公共节点。

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 分别计算两个链表长度，长的先走差值步数，再同时走
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        numA = numB = 0
        pa, pb = headA, headB
        while pa:
            numA += 1
            pa = pa.next
        while pb:
            numB += 1
            pb = pb.next
        long, short = headA, headB
        if numB > numA:
            long, short = headB, headA
        dif = abs(numA - numB)
        i = 0
        while i < dif:
            long = long.next
            i += 1
        while long and short and long != short:
            long = long.next
            short = short.next
        return long


# 精妙解法：pa, pb指向两个链表，不等时分别向后移动，
# pa为空时转向B链表，pb为空时转向A链表，直到相遇，或者均为null
class Solution1:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        pa = headA
        pb = headB
        while pa is not pb:
            if pa is None:
                pa = headB
                continue
            if pb is None:
                pb = headA
                continue
            pa = pa.next
            pb = pb.next
        return pa
