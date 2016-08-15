class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        f = [False] * (len(s) + 1)
        f[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if f[j] and s[j:i] in wordDict:
                    f[i] = True
                    break
        return f[len(s)]
        
