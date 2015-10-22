class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)
        self.cache = {}

                
        def match(i, j):
            if (i, j) in self.cache:
                return self.cache[(i, j)]
            if j == n:
                return i == m
            if j == n - 1 or p[j + 1] != '*':
                if i < m and (p[j] == '.' or p[j] == s[i]):
                    return match(i + 1, j + 1)
                else:
                    self.cache[(i, j)] = False
                    return False
            
            while i < m and (p[j] == '.' or p[j] == s[i]):
                if match(i, j + 2):
                    self.cache[(i, j)] = True
                    return True
                i += 1
            return match(i, j + 2)
        print self.cache
        return match(0, 0)
solution = Solution()
print solution.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c")
