# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    firstElement, secondElement = None, None
    prevElement = TreeNode(-sys.maxint-1)
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.traverse(root)
        firstElement.val, secondElement.val = secondElement.val, firstElement.val
    def traverse(root):
        if root == None:
            return
        self.traverse(root.left)
        if self.firstElement == None and self.prevElement.val >= root.val:
            self.firstElement = self.prevElement
        if self.firstElement != None and self.prevElement.val >= root.val:
            self.secondElement = root
        self.prevElement = root
        self.traverse(root.right)
        
