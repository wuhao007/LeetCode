class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        
        n = len(s)
        if n < 2:
            return 0
        dp = [0]*n
        dp[0] = 0
        max_len = 0
        for i in range(n):
            if s[i] == '(':
                dp[i] == 0
            elif s[i] == ')' and i - 1 >= 0:
                j = i - 1 - dp[i-1]
                if j >= 0 and s[j] == '(':
                    dp[i] = dp[i-1] + 2
                    if j - 1 >= 0:
                        dp[i] += dp[j-1]
            max_len = max(max_len, dp[i])    
                    
        return max_len
solution = Solution()
print solution.longestValidParentheses('())')

