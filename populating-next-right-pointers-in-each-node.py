# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root == None:
            return 
        queue = [(root, 0)]
        tree_node = (root, 0)
        while len(queue) > 0:
            node = queue.pop(0)
            if node[0].left != None:
                queue += [(node[0].left, node[1] + 1)]
            if node[0].right != None:
                queue += [(node[0].right, node[1] + 1)]
            if tree_node[1] == node[1]:
                tree_node[0].next = node[0]
            tree_node = node
tree_node = TreeNode(0)
solution = Solution()
solution.connect(tree_node)
