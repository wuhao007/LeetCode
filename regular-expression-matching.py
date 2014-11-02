class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        if s == '':
            return p == ''
        pn = len(p)
        sn = len(s)
        if pn < 2:
            if sn == 1 and (p == s or p == '.'):
                return True
            else:
                return False
        if p[1] != '*':
            return len(s) > 0 and (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p[1:])
        while len(s) > 0 and (s[0] == p[0] or p[0] == '.'):
            if self.isMatch(s, p[2:]):
                return True
            s = s[1:]
        return self.isMatch(s, p[2:])

solution = Solution()
print solution.isMatch('aa','a')
print solution.isMatch('aa','aa')
print solution.isMatch('aaa','aa')
print solution.isMatch('aa','a*')
print solution.isMatch('aa','.*')
print solution.isMatch('ab','.*')
print solution.isMatch('aab','c*a*b')
print solution.isMatch('a','ab*')
print solution.isMatch('a','ab*a')
print solution.isMatch('bbbba','.*a*a')
print solution.isMatch('aaaaaaaaaaaaab','a*a*a*a*a*a*a*a*a*a*c')
print solution.isMatch('caaabbacbabccabaacb','a*b*.*c*c*.*b*abbc');
print solution.isMatch('aaa','a*a')
print solution.isMatch('baa','.ba')
print solution.isMatch('','.*')
print solution.isMatch('aaba','ab*a*c*a')
