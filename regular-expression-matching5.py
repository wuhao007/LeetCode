class Solution(object):
    def matchFirst(self, s, p):
        if s == '' or p == '':
            return False
        a = s[0]
        b = p[0]
        return (b == '.' and a != '') or a == b 
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        print s, p
        if p == '':
            return s == ''
        if len(p) >= 2 and p[1] == '*':
            p2 = p[2:]
            if self.matchFirst(s, p2):
                return True
            
            while self.matchFirst(s, p):
                s = s[1:]
                if self.isMatch(s, p2):
                    return True
        else:
            if self.matchFirst(s, p):
                return self.isMatch(s[1:], p[1:])
        return False
solution = Solution()
print solution.isMatch('aa', 'b*a')


