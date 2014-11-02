class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        i = 0
        j = 0
        has_star = False
        pre_s = i
        pre_p = j
        while i < len(s):
            if j < len(p):
                if s[i] != p[j]:
                    if p[j] == '?':
                        i += 1
                        j += 1
                    elif p[j] == '*':
                        has_star = True
                        pre_s = i
                        pre_p = j
                        while j < len(p) and p[j] == '*':
                            j += 1
                        if j == len(p):
                            return True
                    elif has_star:
                        pre_s += 1
                        i = pre_s
                        j = pre_p
                    else:
                        return False
                else:
                    i += 1
                    j += 1
            elif has_star:
                pre_s += 1
                i = pre_s
                j = pre_p
            else:
                return False

        while j < len(p) and p[j] == '*':
            j += 1
        return j == len(p)
solution = Solution()
print solution.isMatch("aa","a") == False
print solution.isMatch("aa","aa") == True
print solution.isMatch("aaa","aa") == False
print solution.isMatch("aa", "*") == True
print solution.isMatch("aa", "a*") == True
print solution.isMatch("ab", "?*") == True
print solution.isMatch("aab", "c*a*b") == False
print solution.isMatch("aaabbbaaabbabbaabaa", "*aba*b*") == False
print solution.isMatch("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "*aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa*") == True
print solution.isMatch("hi", "*?") == True
print solution.isMatch("abced", "abc*d") == True
