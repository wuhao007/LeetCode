class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        h = {}
        for c in s:
            h[c] = h.get(c, 0) + 1
        m = ''
        for k, v in h.items():
            if v % 2 == 1:
                if m == '':
                    m = k
                else:
                    return []
        
        r = []
        print m
        if m == '':
            self.dfs(h, '', r)
        else:
            h[m] -= 1
            self.dfs(h, m, r)
        return r

    def dfs(self, h, s, r): 
        
        if len(h) == 0:
            r += [s]
            
        for c in h:
            if h[c] > 0:
                h[c] -= 2
                if h[c] == 0:
                    h.pop(c, None)
                self.dfs(h, c + s + c, r)
                h[c] = h.get(c, 0) + 2
solution = Solution()
print solution.generatePalindromes('a')
