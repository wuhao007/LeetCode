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
        start = head
        while start != None:
            node = start
            start = start.next
            while node != None:
                left_list_node = node
                middle_list_node = left_list_node.next
                right_list_node = middle_list_node.next

                left_tree_node = TreeNode(left_list_node.val)
                middle_tree_node = TreeNode(middle_list_node.val)
                right_tree_node = TreeNode(right_list_node.val)

                middle_tree_node.left = left_list_node
                middle_tree_node.right = right_tree_node

                next_left_list_node = middle_list_node
                next_middle_list_node = right_list_node.next

                next_left_list_node.next = next_middle_list_node

                node = next_middle_list_node.next 

