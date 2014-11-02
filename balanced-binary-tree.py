# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        def dfs(node):
            if node == None:
                return (0, True)
            left = dfs(node.left)
            if left[1] == False:
                return (0, False)
            right = dfs(node.right)
            if right[1] == False:
                return (0, False)
            if abs(left[0] - right[0]) > 1:
                return (0, False)
            return (max(left[0], right[0]) + 1, True)
        result = dfs(root)
        return result[1]
node1 = TreeNode(1)
node2 = TreeNode(1)
node3 = TreeNode(1)
node1.left = node2
node1.right = node3
solution = Solution()
solution.isBalanced(node1)
