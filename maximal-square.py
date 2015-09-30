class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        size = [[0] * n for i in range(2)]
        maxsize = 0
        for j in range(n):
            size[0][j] = 1 if matrix[0][j] == '1' else 0
            maxsize = max(maxsize, size[0][j])
        print 0, size[0]
        for i in range(1, m):
            size[i % 2][0] = 1 if matrix[i][0] == '1' else 0
            maxsize = max(maxsize, size[i % 2][0])
            for j in range(1, n):
                if matrix[i][j] == '1':
                    size[i % 2][j] = min(size[(i - 1) % 2][j - 1], size[(i - 1) % 2][j], size[i % 2][j - 1]) + 1
                    maxsize = max(maxsize, size[i % 2][j])
                else:
                    size[i % 2][j] = 0
            print i, size[i % 2]
        return maxsize * maxsize
solution = Solution()
print solution.maximalSquare(["101101","111111","011011","111010","011111","110111"])
print solution.maximalSquare(["11","11"])
