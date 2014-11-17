class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        slen = len(s)
        plen = len(p)
        dp = [[False] * (plen + 1) for _ in range(slen + 1)]
        dp[0][0] = True
        
        for pi in range(2, plen + 1, 2):
            if p[pi - 1] == '*':
                dp[0][pi] = True
            else:
                break
            
        for pi in range(1, plen + 1):
            if p[pi - 1] == '*':
                for si in range(0, slen + 1):
                    if dp[si][pi - 2]:
                        dp[si][pi] = True
                    elif si > 0 and s[si - 1] == p[pi - 2] or :
                        dp[si][pi] = True
                    else:
                        break
            else:
                for si in range(1, slen + 1):
                    if dp[si - 1][pi - 1] and (s[si - 1] == p[pi - 1] or p[pi - 1] == '.'):
                        dp[si][pi] = True
        print dp
        return dp[slen][plen]
solution = Solution()
print solution.isMatch("aa", ".*")
