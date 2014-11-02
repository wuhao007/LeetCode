class TreeNode:
  def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        def generateBranch(nodes):
            if nodes == []:
                return [None]
            elif len(nodes) == 1:
                return [TreeNode(nodes[0])]
            else:
                result = []
                for i in range(len(nodes)):
		    #print nodes[0:i],nodes[i],nodes[i+1:]
                    left_branch = generateBranch(nodes[0:i])
                    right_branch = generateBranch(nodes[i+1:])
                    for left_node in left_branch:
                        for right_node in right_branch:
                            node = TreeNode(nodes[i])
                            node.left = left_node
                            node.right = right_node
                            result += [node]
                return result        
        return generateBranch(range(1, n+1))
solution = Solution()
for node in solution.generateTrees(3):
    print node.val

