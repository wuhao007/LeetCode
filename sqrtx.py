class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        def sqrt(x, n):
            print x, n
            if abs(x * x - n) < 0.01:
                return int(x)
            else:
                return int(sqrt(x - (x*x-n)/(2.0*x), n))
        return sqrt(x, x)
solution = Solution()
print solution.sqrt(1)
