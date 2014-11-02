class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        def hasPathSum(node, total, path, paths):
            if node == None:
                return
            if node.left == None and node.right == None:
                print total, node.val, path, paths
                if total == node.val:
                    paths += [path[:]]
                print total, node.val, path, paths
                return
            if root.left != None:
                path += [node.val]
                hasPathSum(node.left, total-node.val, path, paths)
                path.pop()
            if root.right != None:
                path += [node.val]
                hasPathSum(node.right, total-node.val, path, paths)
                path.pop()
        road = []
        roads = []
        if root == None:
           return []
        if root.left == None and root.right == None:
           if sum == root.val:
               return [sum]
        hasPathSum(root, sum, road, roads)
        return roads
node1 = TreeNode(6)
node2 = TreeNode(-7)
node3 = TreeNode(-6)
node4 = TreeNode(7)
node5 = TreeNode(-4)
node6 = TreeNode(5)
node1.right = node2
node2.left = node3
node2.right = node4
node3.left = node5
node5.right = node6

solution = Solution()
print solution.pathSum(node1,4)
#print solution.pathSum(None, 1)

