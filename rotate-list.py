# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        def removeNthFromEnd(head, n):
            if head.next == None:
                return n-1, head, head
                
            else:
                m, h, t = removeNthFromEnd(head.next, n)
                print m, h, t

                if m == 1:
                    return m - 1, head, t
                if m == 0:
                    head.next = None
                return m - 1, h, t

        if head == None or head.next == None:
            return head
        node = head
        n = 0
        while node != None:
            n += 1
            node = node.next
        k %= n
        if k == 0 or k == n:
            return head
        m, h, t = removeNthFromEnd(head, k)
        
        t.next = head
        return h

node1 = ListNode(1)        
node2 = ListNode(2)        
node3 = ListNode(3)        
node1.next = node2
node2.next = node3
solution = Solution()
solution.rotateRight(node1, 2)


