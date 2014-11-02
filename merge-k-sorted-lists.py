# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
import heapq
class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        n = len(lists)
        if n < 2:
            return lists[0]
        h = []
        for i in range(n):
            if lists[i] != None:
                heapq.heappush(h, (lists[i].val, i))

        head = ListNode(1)
        node = head
        while h != []:
            e = heapq.heappop(h)
            i = e[1]
            node.next = lists[i]
            
            if lists[i].next != None:
                lists[i] = lists[i].next
                heapq.heappush(h, (lists[i].val, i))
            node = node.next
        head = head.next 
        node = head
        while node != None:
            print node.val
            node = node.next
        return head

a = ListNode(0)
b = ListNode(1)
c = ListNode(2)
d = ListNode(3)
e = ListNode(4)
f = ListNode(5)
g = ListNode(6)
h = ListNode(7)
i = ListNode(8)
j = ListNode(9)
a.next = f
b.next = g
c.next = h
d.next = i
e.next = j
l = [a,b,c,d,e]
solution = Solution()
solution.mergeKLists(l)
