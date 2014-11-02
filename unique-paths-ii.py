class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
    
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        count = []
        for i in range(m):
            count += [[0]*n]

        if obstacleGrid[0][0] == 0:
            count[0][0] = 1
        print count
        for i in range(0,m):
            for j in range(0,n):
                if i == j == 0:
                    continue
                if obstacleGrid[i][j] == 0:
                    count[i][j] = 0
                    if i > 0:
                        count[i][j] += count[i-1][j]
                    if j > 0:
                        count[i][j] += count[i][j-1]
                    print i, j, count[i][j]
                else:
                    count[i][j] = 0 
                    print i, j, count[i][j]
        print count
        return count[m-1][n-1]
solution = Solution()
solution.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
