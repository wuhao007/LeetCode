class Solution:
    """
    @param a, b, n: 32bit integers
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        result = 1
        while b > 0:
            if b % 2 == 1:
                result *= a
            print a, result
            a = (a * a) % b;
            b /= 2
        return result % b
solution = Solution()
print solution.fastPower(3,4,7)

