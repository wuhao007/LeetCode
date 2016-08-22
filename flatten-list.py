class Solution(object):

    # @param nestedList a list, each element in the list 
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        # Write your code here
        print nestedList
        if type(nestedList) is list:
            return reduce(lambda x, y: self.flatten(x) + self.flatten(y), nestedList)
        else:
            return [nestedList]
solution = Solution()
print solution.flatten([1,[4,[6]]])

