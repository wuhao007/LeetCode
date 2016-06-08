# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder == None or postorder == None or len(inorder) != len(postorder):
            return None
        hm = {}
        for i, val in enumerate(inorder):
            hm[val] = i
        return self.buildTreePostIn(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1, hm)
    def buildTreePostIn(self, inorder, ins, ine, postorder, pos, poe, hm):
        if pos > poe or ins > ine:
            return None
        root = TreeNode(postorder[pe])
        ri = hm.get(root)
        root.left = self.buildTreePostIn(inorder, ins, ri - 1, postorder, pos, pos + ri - ios - 1, hm)
        root.left = self.buildTreePostIn(inorder, ri + 1, ine, postorder, pos + ri - ios, poe -1, hm)
        return root
  

