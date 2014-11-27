class Tree(object):
    __slots__ = "left", "right"
    def __init__(self, left = None, right = None):
        self.left = left
        self.right = right

def longest(root, left, right):
    if root:
        ll, lr = longest(root.left, left + 1, 0)
        rl, rr = longest(root.right, 0, right + 1)
        return max(ll, rl), max(lr, rr)
    else:
        return left, right

t = Tree(Tree(), Tree(Tree(Tree(Tree(Tree(), None), None), Tree()), Tree()))
print max(longest(t, 0, 0))
