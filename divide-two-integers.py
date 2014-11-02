class Solution:
    # @return an integer
    def divide(self, dividend, divisor, n = 0):
        print dividend, divisor, n
        if dividend < 0:
            return -self.divide(-dividend, divisor, 0)
        if divisor < 0:
            return -self.divide(dividend, -divisor, 0)
        if dividend == 0:
            return 0
        if divisor == 0:
            return None
        elif dividend > divisor:
            return self.divide(dividend, long(divisor<<1), n + 1)
        elif dividend == divisor:
            if n > 0:
                return long(1<<n)
            else:
                return 1
        else:
            if n > 0:
                return long(1<<(n-1)) + self.divide(dividend - (divisor>>1), divisor>>n, 0)
            else:
                return 0
solution = Solution()
print solution.divide(2147483647,1)
