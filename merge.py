class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        i = 0
        j = 0
        while i < m and j < n:
            if A[i] > B[j]:
                A.insert(i, B[j])
                j += 1
                i += 1
            else:
                i += 1
        while j < n:
            A += [B[j]]
            j += 1
s=Solution()
A = []
B = [1]
s.merge(A,0,B,1)
print A