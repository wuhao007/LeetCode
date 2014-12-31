class TreeNode():
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def average_value_each_level(root):
    queue = [root]
    average = []
    while queue:
        size = len(queue)
        total = 0
        for _ in range(size):
            node = queue.pop(0)
            total += node.val
            if node.left:
                queue += [node.left]
            if node.right:
                queue += [node.right]
        average += [float(total) / size]
    return average      

def average_value_each_level_recursive(root, level, average):
    if root:
        if len(average) <= level:
            average += [(root.val, 1)]
        else:
            average[level] = (average[level][0] + root.val, average[level][1] + 1)
        average_value_each_level_recursive(root.left, level + 1, average)
        average_value_each_level_recursive(root.right, level + 1, average)
    return map(lambda x : float(x[0]) / x[1], average)

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
print average_value_each_level(node1)
print average_value_each_level_recursive(node1, 0, [])
