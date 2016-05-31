class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        cur = [[grid[0][0]] * n for _ in range(2)]
        for j in range(1, n):
            cur[0][j] = cur[0][j - 1] + grid[0][j]
        for i in range(1, m):
            cur[i%2][0] = cur[(i-1)%2][0] + grid[i][0]
            for j in range(1, n):
                cur[i%2][0] = min(cur[(i-1)%2][0], cur[i%2][j-1]) + grid[i][0]
        return cur[(m - 1)%2][n-1]
                 
        
        
