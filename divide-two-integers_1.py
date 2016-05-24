class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return sys.maxint
        sign == 1 if (dividend < 0) ^ (divisor < 0) == 0 else -1
        dvd, dvs = abs(dividend), abs(divisor)
        res = 0
        while dvd >= dvs:
            temp = dvs
            multiple = 1
            while dvd >= (temp << 1):
                temp << = 1
                multiple <<= 1
            dvd -= temp
            res += multiple
        return res if sign == 1 else -res
        
