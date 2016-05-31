class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        cur = [[1] * n for _ in range(2)]
        for i in range(1, m):
            cur[i%2][0] = cur[(i-1)%2][0]
            for j in range(1, n):
                cur[i%2][j] = cur[(i-1)%2][j] + cur[i%2][j-1]
        return cur[(m-1)%2][j]
