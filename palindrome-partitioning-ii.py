class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        n = len(s)
        matrix = []
        if len(s) <= 1:
            return 0
        for i in range(n):
            matrix += [[False]*n]
        cut = []
        for i in range(n+1):
            cut += [n - i - 1]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (i == j or i + 1 == j or matrix[i+1][j-1]):
                    matrix[i][j] = True
                    cut[i] = min(cut[i], cut[j+1]+1)
        return cut[0]
solution = Solution()
print solution.minCut('aab')
