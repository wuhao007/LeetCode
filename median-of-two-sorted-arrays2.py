class Solution:
    """
    @param A: An integer array.
    @param B: An integer array.
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        # write your code here
        def findKth(A, A_start, B, B_start, k):
            if A_start >= len(A):
                return B[B_start + k - 1]
            if B_start >= len(B):
                return A[A_start + k - 1]
            if k == 1:
                return min(A[0], B[0])
            A_key = A[A_start + k / 2 - 1] if A_start + k / 2 - 1 < len(A) else sys.maxint
            B_key = B[B_start + k / 2 - 1] if B_start + k / 2 - 1 < len(B) else sys.maxint
            if A_key < B_key:
                return findKth(A, A_start + k / 2, B, B_start, k - k / 2)
            else:
                return findKth(A, A_start, B, B_start + k / 2, k - k / 2)
        n = len(A) + len(B)
        if n % 2 == 0:
            return findKth(A, A_start, B, B_start, k / 2) + findKth(A, A_start, B, B_start, k / 2 + 1)
        else:
            return findKth(A, A_start, B, B_start, k / 2)

