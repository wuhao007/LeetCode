class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        n = len(A)
        if n < 3:
            return n
        j = -1
        twice = False
        for i in range(len(A)):
            a = A[i]
            if j < 0:
                j = 0
                A[j] = a 
            elif a > A[j]:
                j += 1
                A[j] = a
                twice = False
            elif twice == False:
                j += 1
                A[j] = a
                twice = True
        A = A[:j+1]
        return len(A)
solution = Solution()
print solution.removeDuplicates([1,1,1,2])

