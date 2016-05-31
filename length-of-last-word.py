class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        n = len(s)
        for i in range(n):
            if s[i] != ' ':
                l += 1
            elif i + 1 < n and s[i + 1] != ' ':
                l = 0
        return l
