class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        hashset = {}
        positive = True

        if numerator == 0:
            return '0'
        elif numerator < 0:
            positive = not positive
            numerator = abs(numerator)

        if denominator < 0:
            positive = not positive
            denominator = abs(denominator)

        remainder = numerator % denominator

        if remainder is 0:
            return ('' if positive else '-') + str(numerator / denominator) 
        ret = str(numerator / denominator) + '.'
        print 'remainder' + str(remainder)
        while True:
            hashset[remainder] = len(ret)
            remainder = remainder * 10
            ret += str(remainder / denominator)
            remainder = remainder % denominator
            print 'remainder' + str(remainder)
            if remainder == 0:
                return ('' if positive else '-') + ret
            if remainder in hashset:
                k = hashset[remainder]
                return ('' if positive else '-') + ret[:k] + '(' + ret[k:] + ')'
solution = Solution()
print solution.fractionToDecimal(1, 2)
print solution.fractionToDecimal(2, 1)
print solution.fractionToDecimal(2, 3)
print solution.fractionToDecimal(-1, -2147483648)

