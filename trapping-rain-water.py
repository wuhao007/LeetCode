class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        n = len(A)
        
        r = [0]*n
        r[0] = A[0]
        for i in range(1, n):
            r[i] = max(r[i-1], A[i])
        
        l = [0]*n
        l[n-1] = A[n-1]
        for i in range(n-2, -1, -1):
            l[i] = max(l[i+1], A[i])
        
        water = 0
        for i in range(n):
            water += (min(l[i], r[i]) - A[i])

        return water
solution = Solution()
print solution.trap([0,1,0,2,1,0,1,3,2,1,2,1])
