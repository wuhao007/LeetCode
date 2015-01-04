class Solution:
    def sqrt(self, n):
        def sqrt(x, n):
            return x if abs(x * x - n) <= 0.001 else sqrt(x - (x*x-n)/(2.0*x), n)
        return sqrt(n, n)
solution = Solution()
print solution.sqrt(4)
print solution.sqrt(5)
print solution.sqrt(6)
print solution.sqrt(7)
print solution.sqrt(8)
print solution.sqrt(9)
