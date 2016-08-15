# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        return self.sumR(root, 0)
    def sumR(self, root, x):
        if root.right == root.left == None:
            return 10 * x + root.val
        val = 0
        if root.left:
            val = self.sumR(root.left, 10 * x + root.val)
        if root.right:
            val += self.sumR(root.right, 10 * x + root.val)
        return val
