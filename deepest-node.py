class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class Solution:
    def bfs(self, root):
        queue = [root]
        last = []
        while len(queue) > 0:
            size = len(queue)
            last = queue[:]
            for _ in range(size):
                node = queue.pop()
                if node.left:
                    queue += [node.left]
                if node.right:
                    queue += [node.right]
        return last            
nodea = Node('a')
nodeb = Node('b')
nodec = Node('c')
noded = Node('d')
nodee = Node('e')
nodef = Node('f')
nodeg = Node('g')
nodeh = Node('h')
nodea.left = nodeb
nodea.right = nodec
nodeb.left = noded
nodeb.right = nodee
nodec.left = nodef
nodec.right = nodeg
noded.right = nodeh
solution = Solution()
last = solution.bfs(nodea)
print last[0].key
