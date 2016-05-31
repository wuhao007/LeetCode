class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i = j = 0
        match = 0
        starIdx = -1
        while i < len(s):
           if j < len(p) and p[j] == '?' or s[i] == p[j]:
                i, j = i + 1, j + 1
            elif j < len(p) and p[j] == '*':
                starIdx = j
                match = i
                j += 1
            elif starIdx != -1:
                j = starIdx + 1
                match += 1
                i = match
            else:
                return False
        while j < len(p) and p[j] == '*':
            j += 1
        return j == len(p)
 
