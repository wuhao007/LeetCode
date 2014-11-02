# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if inorder == [] or preorder == []:
            return None
        else:
            root = TreeNode(preorder[0])
            it = 0
            for i in range(len(inorder)):
              if inorder[i] == root.val:
                  it == i
                  break
            root.left = self.buildTree(inorder[0:it], preorder[1:it+1])
            root.right = self.buildTree(inorder[it+1:], preorder[it+1:])
            print root.left, root.right
            return root        
solution = Solution()
solution.buildTree([1,2],[2,1])
