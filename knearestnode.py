class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
from heapq import heappush, heappop, heappushpop
class KNearestNode:
    def __init__(self, k, val):
        self.k = k
        self.val = val
        self.pq = []
        self.stack = []
        self.count = 0

    def KNearest(self, val):
        mn = -abs(val - self.val)
        if (mn, val) in self.pq or val == self.val:
            return 
        if len(self.pq) >= self.k:
            heappushpop(self.pq, (mn, val))
        else:
            heappush(self.pq, (mn, val))
        self.count += 1

    def find(self, node):
        if node.val is self.val:
            return node
        else:
            self.stack += [node]
            if self.val < node.val:
                return self.find(node.left)
            else:
                return self.find(node.right)

    def inorder_forward(self, node):
        if node is None or self.count > self.k:
            return
        if node.left:
            self.inorder_forward(node.left)
        self.KNearest(node.val)
        print self.pq, "forward", node.val
        if node.right:
            self.inorder_forward(node.right)

    def inorder_backward(self, node):
        if node is None or self.count > self.k:
            return
        if node.right:
            self.inorder_backward(node.right)
        self.KNearest(node.val)
        print self.pq, "backward", node.val
        if node.left:
            self.inorder_backward(node.left)

    def find_k_nearest(self, root):
        the_node = self.find(root)
        print [x.val for x in self.stack]
        print self.stack
        self.count = 0
        self.inorder_forward(the_node.right)
        self.count = 0
        self.inorder_backward(the_node.left)
        while len(self.pq) < self.k:
            node = self.stack.pop()
            self.count = 0
            self.inorder_forward(node)
            self.count = 0
            self.inorder_backward(node)

        return sorted([heappop(self.pq)[1] for _ in range(self.k)])

node0 = TreeNode(0)
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)
node9 = TreeNode(9)
node5.left = node2
node5.right = node8
node2.left = node1
node1.left = node0
node2.right = node3
node3.right = node4
node8.left = node7
node7.left = node6
node8.right = node9

solution = KNearestNode(4, 9)
print solution.find_k_nearest(node5)

