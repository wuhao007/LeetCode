class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        n = len(s)
        while i < n and s[i] == ' ':
            i += 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            i += 1
        
        n_nm = 0
        n_pt = 0
        while i < n and ('0' <= s[i] <= '9' or s[i] == '.'):
            if s[i] == '.':
                n_pt += 1
            else:
                n_nm += 1
            i += 1
        if n_pt > 1 or n_nm < 1:
            return False
        if i < n and s[i] == 'e':
            i += 1
            if i < n and (s[i] == '+' or s[i] == '-'):
                i += 1
            n_nm = 0
            while i < n and s[i] >= '0' and s[i] <= '9':
                i += 1
                n_nm += 1
            if n_nm < 1:
                return False
        while i < n and s[i] == ' ':
            i += 1
        return i == n 
