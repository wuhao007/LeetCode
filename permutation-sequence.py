import math
class Solution:
    # @return a string
    def getPermutation(self, n, k):
        def getPermutation(n):
            if n < 1:
                return 1
            else:
                return n * getPermutation(n-1)
        p = getPermutation(n-1)
        a = ""
	lst = range(1, n+1)
        for i in range(n-1):
            print lst, k, p
            a += str(lst.pop(int(math.ceil(k*1.0/p))-1))
            k %= p
            p /= (n-i-1)
        a += str(lst.pop())
        return a
        
solution = Solution()
print solution.getPermutation(3,1)
