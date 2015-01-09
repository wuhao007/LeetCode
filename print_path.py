class TreeNode:
    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None

def print_path(root):
    queue_node = [(root, root.label)]
    while queue_node:
        node, path = queue_node.pop(0)
        if node.left:
            queue_node += [(node.left, path + node.left.label)]
        if node.right:
            queue_node += [(node.right, path + node.right.label)]
        if node.left is None and node.right is None:
            print path

node_a = TreeNode('a')
node_b = TreeNode('b')
node_c = TreeNode('c')
node_d = TreeNode('d')
node_e = TreeNode('e')
node_f = TreeNode('f')
node_g = TreeNode('g')
node_a.left = node_b
node_a.right = node_c
node_b.left = node_d
node_b.right = node_e
node_c.left = node_f
node_c.right = node_g
            
print_path(node_a)
