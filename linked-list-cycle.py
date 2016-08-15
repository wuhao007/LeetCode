# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        walker, runner = head, head
        while runner.next != None and runner.next.next != None:
            walker, runner = walker.next, runner.next.next
            if walker == runner:
                return True
        return False
            
