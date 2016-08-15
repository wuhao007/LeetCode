class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return '0'
        res = ''
        if n < 0 ^ d < 0:
            res += '-'
        n, b = abs(numerator), abs(denominator)
        res += str(n / d)
        if n % d == 0:
            return res
        res += '.'
        mp = {}
        r = n % d
        while r:
            if r in mp:
                return res[:mp[r]] + '(' + res[mp[r]:] + ')'
            mp[r] = len(res)
            r *= 10
            res += str(r / d)
        return res
