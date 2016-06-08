class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        n = len(s)
        while i < 4 and i < n - 2:
            j = i + 1
            while j < i + 4 and j < n - 1:
                k = j + 1
                while k < j + 4 and k < n:
                    s1, s2, s3, s4 = s[:i], s[i:j], s[j:k], s[k:n]
                    if self.isValid(s1) and self.isValid(s2) and self.isValid(s3) and self.isValid(s4):
                        res.append('.'.join(s1, s2, s3, s4)
                    k += 1
                j += 1
            i += 1
        return res

    def isValid(self, s):
        if len(s) > 3 or len(s) == 0 or (s[0] == '0' and len(s) > 1) or int(s) > 255):
            return False
        return True
