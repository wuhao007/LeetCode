# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.val)

class Solution:
    # @param root, a tree node
    # @return a tree node

    def recoverTree(self, root):
        def checkTreeLeft(root, queue):
            if len(queue) >= 2:
                queue.pop(0)
            
            queue += [root]
            if len(queue) < 2:
                return False
            elif queue[0].val > queue[1].val:
                return True
            else:
                return False
                
        def checkTreeRight(root, queue):
            if len(queue) >= 2:
                queue.pop(0)
            
            queue += [root]
            if len(queue) < 2:
                return False
            elif queue[0].val < queue[1].val:
                return True
            else:
                return False
                
        def tranTreeLeft(root, queue):
            if root == None:
                return False
            else:
                if tranTreeLeft(root.left, queue):
                    return True
                if checkTreeLeft(root, queue):
                    return True
                if tranTreeLeft(root.right, queue):
                    return True
                    
        def tranTreeRight(root, queue):
            if root == None:
                return False
            else:
                if tranTreeRight(root.right, queue):
                    return True
                if checkTreeRight(root, queue):
                    return True
                if tranTreeRight(root.left, queue):
                    return True                

        
        node1 = None
        node2 = None
        queue1 = []
        if tranTreeLeft(root, queue1):
            node1 = queue1[0]
        queue2 = []
        if tranTreeRight(root, queue2):
            node2 = queue2[0]
        node1.val, node2.val = node2.val, node1.val
        return root

node0 = TreeNode(0)
node1 = TreeNode(1)
node0.left = node1
solution = Solution()
solution.recoverTree(node0)
