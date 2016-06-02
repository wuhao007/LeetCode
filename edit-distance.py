class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(2)]
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            dp[i%2][0] = i
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i%2][j] = dp[(i-1)%2][j-1]
                else:
                    dp[i%2][j] = min(dp[(i-1)%2][j-1], dp[i%2][j-1], dp[(i-1)%2][j]) + 1
        return dp[m%2][n]         
            
         
