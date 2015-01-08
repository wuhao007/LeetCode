# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return root of the upside down tree
    def upsideDownBinaryTree(self, root):
        '''
        p.left = parent.right
        p.right = parent
        '''
        def dfsBottomUp(p, parent):
            if p is None:
                return parent
            root = dfsBottomUp(p.left, p)
            p.left = parent if parent is None else parent.right
            p.right = parent
            return root
        return dfsBottomUp(root, None)
