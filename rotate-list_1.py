# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        ln = 1
        if not head:
            return head
        newH = tail = head
        while tail.next:
            tail = tail.next
            ln += 1
        tail.next = head
        k %= ln
        if k:
            for i in range(ln - k):
                tail = tail.next
        newH = tail.next
        tail.next = None
        return newH
