class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    # @param A: Given an integer array with no duplicates.
    # @return: The root of max tree.
    def maxTree(self, A):
        # write your code here
        stack = []
        root = None

        for a in A:
            node = TreeNode(a)
            if root is None or root.val < a:
                root = node
            if stack:
                if stack[-1].val > a:
                    stack += [node]
                else:
                    child = stack.pop()
                    while len(stack) > 0 and stack[-1].val < a:
                        stack[-1].right = child
                        child = stack.pop()
                    if stack:
                        stack[-1].right = node
                    node.left = child
                    stack += [node]
                print map(lambda x : x.val, stack) 
            else:
                stack += [node]
        return root
solution = Solution()
solution.maxTree([2,5,6,0,3,1])
