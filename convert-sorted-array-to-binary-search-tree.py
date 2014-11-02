class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        length = len(num)
        if length == 0:
            return None
        if length == 1:
            return TreeNode(num[0])
        mid = length/2
        left_node = self.sortedArrayToBST(num[:mid])
        right_node = self.sortedArrayToBST(num[mid + 1:])
        mid_node = TreeNode(num[mid])
        mid_node.left = left_node
        mid_node.right = right_node
        return mid_node
        
