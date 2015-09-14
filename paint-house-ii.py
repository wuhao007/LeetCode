import sys
class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        if n == 0:
            return 0
        k = len(costs[0])
        f = [[sys.maxint] * k for i in range(2)]
        for j in range(k):
            f[0][j] = costs[0][j]
        for i in range(1, n):
            for j in range(k):
                f[i % 2][j] = min(f[(i - 1) % 2][(j - 1) % k], f[(i - 1) % 2][(j + 1) % k]) + costs[i][j]
        return min(f[(n - 1) % 2])        
solution = Solution()
print solution.minCostII([[15,17,15,20,7,16,6,10,4,20,7,3,4],[11,3,9,13,7,12,6,7,5,1,7,18,9]])


