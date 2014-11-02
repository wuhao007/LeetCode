class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class KNearestNode:
    import heapq
    def __init__(self):
        self.pq = []
    def find(self, head, val):
        if node.val is val:
            return head
        else:
            if val < node.val:
                return self.find(node.left, val)
            else:
                return self.find(node.right, val)
