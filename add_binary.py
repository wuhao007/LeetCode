class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        def addBinary(a, b, c):
            if a == '':
                if c == 0:
                    return ''
                else:
                    return '1'
            if b == '':
                if c == 0:
                    return a
                else:
                    return addBinary(a, str(c), 0)
            s = int(a[-1]) + int(b[-1]) + c
            if s == 0:
                return addBinary(a[:-1], b[:-1], 0) + '0'
            elif s == 1:
                return addBinary(a[:-1], b[:-1], 0) + '1'
            elif s == 2:
                return addBinary(a[:-1], b[:-1], 1) + '0'
            elif s == 3:
                return addBinary(a[:-1], b[:-1], 1) + '1'
        if len(a) > len(b):
            return addBinary(a, b, 0)
        else:
            return addBinary(b, a, 0)
solution = Solution()
print solution.addBinary('0','0')
