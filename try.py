# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        def dfs(root):
            if root.left == None and root.right == None:
                return root
            else:
                left = root.left
                right = root.right
                head = None
                if left != None:
                    root.right = left
                    head = dfs(left)
                    if right != None:
                        head.right = right
                        head = dfs(right)
                else:
                    root.right = right
                    head = dfs(right)
                return head
        if root == None:
            return root
        h = root
        dfs(h)
        return root
t0 = TreeNode(0)
t1 = TreeNode(1)
t2 = TreeNode(2)
#t3 = TreeNode(3)
#t4 = TreeNode(4)
#t5 = TreeNode(5)
#t6 = TreeNode(6)
t1.right = t2
#t1.right = t5
#t2.left = t3
#t2.right = t4
#t5.right = t6
s = Solution()
s.flatten(t1)
h = t1
while h != None:
    print h.val
    h = h.right
