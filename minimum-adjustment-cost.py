class Solution:
    # @param A: An integer array.
    # @param target: An integer.
    def MinAdjustmentCost(self, A, target):
        # write your code here
        n = len(A)
        f = [[65535] * 10 for _ in range(n)]
        for v in range(10):
            f[0][v] = abs(A[0] - v)
        print f
        for i in range(1, n):
            for v in range(10):
                cost = abs(A[i] - v)
                for w in range(10):
                    if abs(v - w) <= target:
                        f[i][v] = min(f[i][v], f[i - 1][w] + cost)
        print f
        return min(f[n - 1])  
solution = Solution()
print solution.MinAdjustmentCost([1,4,2,3], 1)
