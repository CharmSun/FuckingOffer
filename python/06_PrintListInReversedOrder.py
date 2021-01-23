# 题目：从尾到头打印链表
# 输入一个链表的头节点，从尾到头反过来打印出每个节点的值

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # 栈
    def printListFromTailToHead(self, head: ListNode) -> None:
        stack = []
        p = head
        while p:
            stack.append(p)
            p = p.next
        while stack:
            node = stack.pop()
            print(node.val)
