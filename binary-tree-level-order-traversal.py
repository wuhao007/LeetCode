# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        level_order = []
        queue = [root]
        levels = [0]
        while len(queue) > 0:
            node = queue.pop(0)
            level = levels.pop(0)
            if level < len(level_order):
                level_order[level] += [node]
            else:
                level_order += [[node]]
            if node.left != None:
                queue += [node.left]
                levels += [level + 1]
            if node.right != None:
                queue += [node.right]
                levels += [level + 1]
        return level_order

