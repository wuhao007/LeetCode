class Solution:
    """
    @param s: A string 
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        # write your code here
        def is_match(i_s, i_p):
            if i_p == len(p):
                return i_s == len(s)
            elif i_p + 1 < len(p) and p[i_p + 1] == '*':
                if i_s < len(s) and (s[i_s] == p[i_p] or p[i_p] == '.'):
                    return is_match(i_s + 1, i_p) or is_match(i_s, i_p + 2)
                else:
                    return is_match(i_s, i_p + 2)
            else:
                return (i_s < len(s) and (s[i_s] == p[i_p] or p[i_p] == '.')) and is_match(i_s + 1, i_p + 1)
        return is_match(0, 0)
solution = Solution()
print solution.isMatch("aab", "c*a*b")
print solution.isMatch("aa", "a*")
print solution.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c")
