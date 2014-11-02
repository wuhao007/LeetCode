class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        def _removeDuplicates(A):
            if len(A) <= 2:
                return A
            else:
                head = A[0]
                i = 0
                while i < len(A) and head == A[i] :
                    i += 1
                tail = min(i, 2)
                return A[:tail] + _removeDuplicates(A[i:])
        return _removeDuplicates(A)
solution = Solution()
print solution.removeDuplicates([1,1,1,2])
