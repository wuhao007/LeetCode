class TreeNode:
    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None

def print_path(root):
    if root is None:
        return
    stack = [root]
    path = []
    while stack:
        cur = stack.pop()
        if cur.right:
            stack += [cur.right]
        if cur.left:
            stack += [cur.left]
        path += [cur.label]
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

