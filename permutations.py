class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        def dfs(num, path, ret):
            if len(num) == 0:
                ret += [path[:]]
            else:
                for i in range(len(num)):
                    k = num.pop(i)
                    path += [k]
                    dfs(num, path, ret)
                    num.insert(i, k)
                    path.pop()
        ret = []
        dfs(num, [], ret)
        return ret
solution = Solution()
print solution.permute([1])

