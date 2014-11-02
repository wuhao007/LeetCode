class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        n = len(s)
        if n <= 0:
            return 0
        dp = [0]*n
        if 0 < int(s[0]) < 27:
            dp[0] = 1
        for i in range(1,n):
            if 0 < int(s[i]) < 27 and dp[i-1] > 0:
                dp[i] += dp[i-1]
            if int(s[i-1]) > 0 and 0 < int(s[i-1] + s[i]) < 27:
                if i - 2 < 0:
                    dp[i] += 1
                elif dp[i-2] > 0:
                    dp[i] += dp[i-2]
        return dp[-1]
                
solution = Solution()
print solution.numDecodings("01")


