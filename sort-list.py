# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        p, f = head, head.next.next
        while f and f.next:
            p, f = p.next, f.next.next
        h2 = self.sortList(p.next)
        p.next = None
        return self.merge(self.sortList(head), h2)

    def merge(self, h1, h2):
        hn = ListNode(0)
        c = hn
        while h1 and h2:
            if h1.val < h2.val:
                c.next = h1
                h1 = h1.next
            else:
                c.next = h2
                h2 = h2.next
            c = c.next
        if h1:
            c.next = h1
        if h2:
            c.next = h2
        return hn.next
