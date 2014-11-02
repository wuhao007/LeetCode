# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        node_array = []
        while head != None:
            node_array += [head.val]
            head = head.next
        def sortedArrayToBST(num):
            length = len(num)
            if length == 0:
                return None
            if length == 1:
                return TreeNode(num[0])
            mid = length/2
            left_node = sortedArrayToBST(num[:mid])
            right_node = sortedArrayToBST(num[mid + 1:])
            mid_node = TreeNode(num[mid])
            mid_node.left = left_node
            mid_node.right = right_node
            return mid_node        
        return sortedArrayToBST(node_array)
