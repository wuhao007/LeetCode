class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        n = len(A)
        jump = [0] * (n + 1)
        jump[0] = A[0]
        for i in range(1, n):
            if jump[i-1] >= i:
                jump[i] = max(jump[i-1], i + A[i])
            else:
                jump[i] = jump[i-1]
            if jump[i] >= n-1:
                return True
        return False
solution = Solution()
print solution.canJump([2,3,1,1,4])
print solution.canJump([3,2,1,0,4])
