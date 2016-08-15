# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1, p2 = headA, headB
        if p1 == None or p2 == None:
            return None
        while p1 != None and p2 != None and p1 != p2:
            p1, p2 = p1.next, p2.next
            if p1 == p2:
                return p1
            if p1 == None:
                p1 = headB
            if p2 == None:
                p2 = headA
        return p1

