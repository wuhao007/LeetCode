class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        def findKth(a, b, k):
            print 'k', k
            print a, b
            if len(a) > len(b):
                return findKth(b, a, k)
            if len(a) == 0:
                return b[k - 1]
            if k <= 1:
                return min(a[0], b[0])
            pa = min(k/2, len(a) - 1)
            pb = k - pa
            print 'pa',pa, 'pb',pb
            if pa < 1 or pb > len(b):
                pa = 1
                pb = k - 1
            print 'pa',pa, 'pb',pb
            print 'apa',a[pa-1], 'bpb',b[pb-1]
            if a[pa-1] > b[pb-1]:
                return findKth(a, b[pb:], k - pb)
            elif a[pa-1] < b[pb-1]:
                return findKth(a[pa:], b, k - pa)
            else:
                return a[pa-1]
        total = len(A) + len(B)
        if total % 2 == 0:
            a1 = findKth(A, B, total/2)
            print 'a1', a1
            a2 = findKth(A, B, total/2 + 1)
            print 'a2', a2
            return (a1 + a2)/2.0
        else:
            return findKth(A, B, total/2 + 1)
solution = Solution()
print solution.findMedianSortedArrays([1],[2,3,4])
