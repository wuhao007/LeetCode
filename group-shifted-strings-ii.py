class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        def dfs(path, n, result):
            if n <= 0:
                result += [''.join(path)]
            else:
                for k, v in h.items():
                    path.insert(0, k)
                    path.append(v)
                    dfs(path, n - 2, result)
                    path.pop(0)
                    path.pop()
        h = {'1':'1', '0':'0', '8':'8', '6':'9', '9':'6'}
        result = []
        if n % 2 == 0:
            dfs([], n, result)
        else:
            dfs(['0'], n - 1, result)
            dfs(['1'], n - 1, result)
            dfs(['8'], n - 1, result)
        return result
solution = Solution()
print solution.findStrobogrammatic(2)
