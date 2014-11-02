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
        duplicates = False
        pre = None
        while node.next != None:
            next_node = node.next
            if node.val == next_node.val:
                node.next = next_node.next
                duplicates = True
            else:
                if duplicates:
                    pre.next = node
                    duplicates = False
                pre = node
                node = node.next
        return head
