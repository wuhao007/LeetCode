class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        def _singleNumber(A):
            c = 0
            for x in A:
                c = c ^ x
            return c
        c = _singleNumber(A)
        lowbit = c - (c & (c - 1))
        a = []
        b = []
        for x in A:
            if lowbit & x == 0:
                a += [x]
            else:
                b += [x]
        return _singleNumber(a), _singleNumber(b)
solution = Solution()
print solution.singleNumber([1,1,2,2,3,3,4,5])
