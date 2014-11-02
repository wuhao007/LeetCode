class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def partition(self, head, x):
        less = None
        less_head = None
        more = None
        more_head = None
        while head != None:
            if head.val < x:
                if less == None:
                    less_head = head  
                else:
                    less.next = head
                less = head
            else:
                if more == None:
                    more_head = head
                else:
                    more.next = head
                more = head
            head = head.next
        if less != None:
            less.next = more_head
        else:
            less_head = more_head
        return less_head
x1 = ListNode(1)
x2 = ListNode(4)
x3 = ListNode(3)
x4 = ListNode(2)
x5 = ListNode(5)
x6 = ListNode(2)
x1.next = x2
x2.next = x3
x3.next = x4
x4.next = x5
x5.next = x6
s = Solution()
head = s.partition(x1,5)
while head != None:
    print head.val
    head = head.next
