class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        factorial = [1] * (n + 1)
        for i in range(1, n + 1):
            factorial[i] = factorial[i - 1] * i 
        numbers = [chr(i + ord('0')) for i in range(1, n + 1)]
        
        sb = []
        k -= 1
        for i in range(1, n + 1):
            index = k / factorial[n - i]
            sb.append(numbers.pop(index))
            k -= index * factorial[n - i]
        return ''.join(sb)
        
