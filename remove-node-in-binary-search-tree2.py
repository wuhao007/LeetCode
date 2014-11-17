class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    """
    @param root: The root of the binary search tree.
    @param value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """    
    def removeNode(self, root, value):
        # write your code here
        def myDeleteNode(parent, node):
            if node.left:
                maxNodeParent = node
                maxNode = node.left
                while maxNode.right:
                    maxNodeParent = maxNode
                    maxNode = maxNode.right
                if maxNodeParent.left == maxNode:
                    maxNodeParent.left = maxNode.left
                else:
                    maxNodeParent.right = maxNode.left
                maxNode.left = node.left
                maxNode.right = node.right
                if parent.left == node:
                    parent.left = maxNode
                else:
                    parent.right = maxNode
            else:
                if parent.left == node:
                    parent.left = node.right
                else:
                    parent.right = node.right
        def findAndDelete(parent, node):
            if node:
                if node.val == value:
                    myDeleteNode(parent, node)
                elif value < node.val:
                    return findAndDelete(node, node.left)
                else:
                    return findAndDelete(node, node.right)
        dummy = TreeNode(0)
        dummy.left = root
        findAndDelete(dummy, dummy.left)
        return dummy.left
node0 = TreeNode(0)
node1 = TreeNode(1)
node2 = TreeNode(2)
node1.left = node0
node1.right = node2
solution = Solution()
print solution.removeNode(node1, node0).val

