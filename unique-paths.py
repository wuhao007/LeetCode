class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        if m <= 1 or n <= 1:
            return 1
        D = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                    D[i][j] = D[i - 1][j] + D[i][j - 1]
        return D[m - 1][n - 1]
solution = Solution()
print solution.uniquePaths(4,6)
