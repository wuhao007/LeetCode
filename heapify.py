class Solution:
    # @param A: Given an integer array
    # @return: void
    def heapify(self, A):
        # write your code here
        
        def sink(k, N):
            j = 2 * k + 1
            if j < N:
                if j + 1 < N and A[j] > A[j + 1]: 
                    j += 1
                if A[k] > A[j]:
                    A[k], A[j] = A[j], A[k]
                    sink(j, N)
        n = len(A)
        for i in range((n - 2) / 2, -1, -1):
            sink(i, n)
        return A
solution = Solution()
print solution.heapify([3,2,1,4,5])
print solution.heapify([11,23,36,38,40])
