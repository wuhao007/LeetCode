# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = [root, root]
        while q:
            t1 = q.pop()
            t2 = q.pop()
            if t1 == t2 == None:
                continue
            if t1 == None or t2 == None:
                return False
            if t1.val != t2.val:
                retrun False
            q += [t1.left, t2.right, t1.right, t2.left]
        return True
