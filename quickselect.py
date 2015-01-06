class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        k -= 1
        n = len(A)
        def kthLargestElement(k, l, r):
            lo = l
            i = l
            gt = r
            while i <= gt:
                if A[i] < A[lo]:
                    A[i], A[lo] = A[lo], A[i] 
                    i += 1
                    lo += 1
                elif A[i] == A[lo]:
                    i += 1
                else:
                    A[i], A[gt] = A[gt], A[i]
                    gt -= 1
            return (lo, gt) if A[lo] == A[gt] else (lo, lo)

        pl = 0
        pr = len(A) - 1
        nl, nr = kthLargestElement(k, pl, pr)
        print nl, nr, A
        while True:
            if k < nl:
                pr = nl - 1
                nl, nr = kthLargestElement(k, pl, pr)
                print nl, nr, k
            elif nl <= k <= nr:
                return A[nl]
            elif k > nr:
                pl = nr + 1
                nl, nr = kthLargestElement(k, pl, pr)
solution = Solution()
print solution.kthLargestElement(3, [9,3,2,4,8])
print solution.kthLargestElement(10, [1,2,3,4,5,6,8,9,10,7])
