# Definition for a binary tree root.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rootStack = []
        result = []
        if root == None:
            return result
        rootStack.append(root)
        while rootStack:
            root = rootStack.pop()
            result.append(root.val)
            if root.left:
                rootStack.append(root.left)
            if root.right:
                rootStack.append(root.right)
        return result[::-1]            
