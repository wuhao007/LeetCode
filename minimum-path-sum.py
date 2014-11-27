class Solution:
    """
    @param grid: a list of lists of integers.
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        M = len(grid)
        N = len(grid[0])
        s = grid[:]
        for i in range(1, M):
            s[i][0] += s[i - 1][0]
        for i in range(1, N):
            s[0][i] += s[0][i - 1]
        for i in range(1, M):
            for j in range(1, N):
                s[i][j] += min(s[i - 1][j], s[i][j - 1])
        return s[M - 1][N - 1]
s = Solution()
print s.minPathSum([[0]])
