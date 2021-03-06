class Solution:
    #@param n: Given a decimal number that is passed in as a string
    #@return: A string
    def binaryRepresentation(self, n):
        # write you code here
        number = float(n)
        a = int(number)
        res = ''
        if a > 0:
            while a > 0:
                res = str(a % 2) + res
                a /= 2
        else:
            res = '0'
        d = number - int(number)
        if d > 0:
            res += '.'
            s = set()
            while d > 0:
                r = d * 2
                if d in s:
                    return 'ERROR'
                else:
                    s.add(d)                
                if r >= 1:
                    res += '1'
                    d = r - 1
                else:
                    res += '0'
                    d = r
        return res
solution = Solution()
print solution.binaryRepresentation(3.72)
