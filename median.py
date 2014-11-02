class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        m = len(A) 
        n = len(B)
        i = m/2
        j = 0
        while i < m and i >= 0 and j < n and j >=0:
            j = (m+n)/2 - i
            if A[i] == B[j]:
                return A[i]
            elif A[i] > B[j]: 
                i = (i+1+m)/2
            elif A[i] < B[j]: 
                i = (i-1)/2
s = Solution()
print s.findMedianSortedArrays([1,2,3,4,5],[2,3,4,5,6,7,8,9])
