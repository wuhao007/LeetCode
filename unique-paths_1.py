class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m > n:
            return self.uniquePaths(n, m)
        cur = [1] * n
        for j in range(n):
            for i in range(m):
                cur[i] += cur[i - 1]
        return pre[m - 1]
