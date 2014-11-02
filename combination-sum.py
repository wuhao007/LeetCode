class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        def dfs(candidate, route, target, result):
            if target == 0:
                result += [route]
                return True
            elif target < 0:
                return False
            else:
                for i in range(len(candidate)):
                    element = candidate[i]
                    dfs(candidate[i:], route + [element], target - element, result)
        result = []
        route = []
        dfs(sorted(candidates), route, target, result)
        return result
solution = Solution()
print solution.combinationSum([2,3,6,7],7)
