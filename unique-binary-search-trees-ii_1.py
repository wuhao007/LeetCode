# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        self.genTrees(1, n)

    def genTrees(self, start, end):
        lst = []
        if start > end:
            lst.append(None)
            return lst
        if start == end:
            lst.append(TreeNode(start)):
            return lst
        for i in range(start, end + 1):
            left, right = self.genTrees(start, i - 1), self.genTrees(i + 1, end)
            for lnode in left:
                for rnode in right:
                    root = TreeNode(i)
                    root.left = lnode
                    root.right = rnode
                    lst.add(root)
        return lst
                
