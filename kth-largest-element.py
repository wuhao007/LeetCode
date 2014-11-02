import random
class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        n = len(A)
	if n < 10:
            A.sort()
            return A[n-k]
        i = 1
        j = n - 1
	p = random.randrange(0, n)
	print A, p, A[p]
        A[p], A[0] = A[0], A[p]
	print A, 0, A[0]
        while True:
            while A[i] > A[0]:
                i += 1
                if i == n - 1:
                    break;
            while A[j] < A[0]:
                j -= 1
                if j == 0:
                    break;
            if i >= j:
                break
            A[i], A[j] = A[j], A[i]        
        A[0], A[j] = A[j], A[0]
	print A, j, A[j]

        if k == j + 1:
            return A[j]
        elif k < j + 1:
            return self.kthLargestElement(k, A[:j])
        elif j + 1 < k:
            return self.kthLargestElement(k-j-1, A[j+1:])
solution = Solution()
print solution.kthLargestElement(4, [9,3,2,4,8]) == 3
print solution.kthLargestElement(10, [1,2,3,4,5,6,8,9,10,7])



