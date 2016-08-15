# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None:
            return
        p1, p2 = head, head
        while p2.next != None and p2.next.next != None:
            p1, p2 = p1.next, p2.next.next
        preMiddle, preCurrent = p1, p1.next
        while preCurrent.next:
            current = preCurrent.next
            preCurrent.next = current.next
            current.next = preMiddle.next
            preMiddle.next = current
        p1, p2 = head, preMiddle.next
        while p1 != preMiddle:
            preMiddle.next = p2.next
            p2.next = p1.next
            p1.next = p2
            p1 = p2.next
            p2 = preMiddle.next
