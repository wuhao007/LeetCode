def _shortest(tree, x, y):
    if tree:
        left_x, left_y, left_lca = _shortest(tree.left, x, y)
        if left_lca:
            return True, True, left_lca
        right_x, right_y, right_lca = _shortest(tree.right, x, y)
        if right_lca:
            return True, True, right_lca
        found_x = tree is x or left_x or right_x
        found_y = tree is y or left_y or right_y
        return found_x, found_y, tree if found_x and found_y else None
    else:
        return False, False, None

shortest = lambda tree, x, y: _shortest(tree, x, y)[2]

class Tree(object):
    __slots__ = "left", "right"
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

t = Tree(Tree(), Tree(Tree(None, Tree()), Tree()))
print shortest(t, t.right.left.right, t.left) is t
print shortest(t, t.right.left.right, t.right.right) is t.right
print shortest(t, t.right.left.right, t.right) is t.right # lca == y
