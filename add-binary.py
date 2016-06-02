class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        s = ''
        c, i, j = 0, len(a) - 1, len(b) - 1
        while i >=0 or j >=0 or c == 1:
            if i >= 0:
                c += ord(a[i]) - ord('0')
                i -= 1
            if j >= 0:
                c += ord(b[j]) - ord('0')
                j -= 1
            s = chr(c % 2 + ord('0')) + s
            c /= 2
        return s
