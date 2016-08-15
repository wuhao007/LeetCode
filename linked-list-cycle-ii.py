# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return None
        firstp, secondp = head, head
        isCycle = False
        while firstp and secondp:
            firstp = firstp.next
            if secondp.next == None:
                return None 
            secondp = secondp.next.next
            if firstp == secondp:
                isCycle == True
                break
        if not isCycle:
            return None
        firstp = head
        while firstp != secondp:
            firstp, secondp = firstp.next, secondp.next
        return firstp      
