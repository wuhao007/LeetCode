class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:

    '''
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    '''
    def serialize(self, root):
        # write your code here
        if root is None:
            return []
        ret = [root.val]
        queue = [root]
        while len(queue) > 0:
            node = queue.pop(0)
    	    if node.left:
                queue += [node.left]
                ret += [node.left.val]
            else:
                ret += ['#']
            if node.right:
                queue += [node.right]
                ret += [node.right.val]
            else:
                ret += ['#']
        print ret
        return ret

    '''
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    '''
    def deserialize(self, data):
        # write your code here
        n = len(data)
        if n == 0:
            return None
        queue = map(lambda x : None if x == '#' else TreeNode(x), data)
        parent = 0
        child = parent + 1
        while child < n:
            node = queue[parent]
            if node:
                node.left = queue[child]
                node.right = queue[child + 1]
                child += 2
            parent += 1
        return queue[0]
def bfs(root):
    queue = [root]
    while len(queue) > 0:
        node = queue.pop(0)
        if node is None:
            print '#'
        else:
            queue += [node.left, node.right]
            print node.val
solution = Solution()
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node1.right = node2
node = solution.deserialize(solution.serialize(None))
bfs(node)
