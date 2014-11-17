class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.lastVal = 0
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            root.val += self.lastVal
            self.lastVal = root.val
            self.inorder(root.right)
        else:
            return
    def print_tree(self, root):
        if root:
            self.print_tree(root.left)
            print root.val
            self.print_tree(root.right)
        else:
            return

        
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.left = node2
node1.right = node3
solution = Solution()
solution.inorder(node1)
solution.print_tree(node1)
