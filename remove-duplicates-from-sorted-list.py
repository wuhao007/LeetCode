# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None:
            return head
        node = head
        twice = False
        while node.next != None:
            next_node = node.next
            if node.val == next_node.val:
                if twice:
                    node.next = next_node.next
                    twice = False
                else:
                    node = node.next
                    twice = True
            else:
                node = node.next
                twice = False
        return head        
