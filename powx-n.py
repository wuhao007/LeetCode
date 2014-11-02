class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n < 0:
            return 1/self.pow(x,-n)
        elif n == 0:
            return 1
        elif n % 2 == 0:
            return self.pow(x*x, n/2)
        else:
            return x * self.pow(x, n-1)
solution = Solution()
print solution.pow(1.00001, 123456)

