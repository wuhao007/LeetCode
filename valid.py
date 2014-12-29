Hi
class Tree:
    def __init__(self):
        self.val = 0
        self.left = None
        self.right = None
        
        
class Solution:
    def __init__(self):
        self.current = None
       
       
    def validBST(self, node):
        if node is None:
            return True
        
        if node.left:
            if not self.valid(node.left):
                return False

        if self.current is None:
            self.current = node
        
        if self.current.val > node.val:
            return False
        self.current = node
        
        if node.right:
            if not self.valid(node.right):
                return False  
        return True
        
solution = Solution()
solution.validBST(tree)


      3
     / \
    2   4
   /     \
  1       5
 /
9

