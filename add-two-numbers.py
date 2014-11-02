# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        def addTwoNumbers(l1, l2, c):
            if l1 == None and l2 == None:
                if c == 0:
                    return None
                else:
                    return ListNode(1)
            elif l1 == None:
                if c > 0:
                    return addTwoNumbers(ListNode(1), l2, 0)
                else:
                    return l2
            elif l2 == None:
                if c > 0:
                    return addTwoNumbers(l1, ListNode(1), 0)
                else:
                    return l1
            else:
                s = l1.val + l2.val + c
                if s < 9:
                    sn = ListNode(s)
                    sn.next = addTwoNumbers(l1.next, l2.next, 0)
                    return sn
                else:
                    sn = ListNode(s%10)
                    sn.next = addTwoNumbers(l1.next, l2.next, 1)
                    return sn
                    
        node = addTwoNumbers(l1, l2, 0)
        while node != None:
            print node.val
            node = node.next

solution = Solution()
l11 = ListNode(1)
l18 = ListNode(8)
l20 = ListNode(0)
l11.next = l18
solution.addTwoNumbers(l11, l20)
