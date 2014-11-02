class Solution:
    """
    @param nums: A list of integers
    @param k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """
    def maxKSubArrays(self, nums, k):
        # write your code here
        def _maxSubArray(nums):
        # write your code here
            if nums == []:
                return 0
            n = len(nums)
            mx = [0]*n
            mx[0] = nums[0]
            result = mx[0]
            for i in range(1, n):
                mx[i] = max(mx[i-1] + nums[i], nums[i])
                result = max(mx[i], result)
            return result
        n = len(nums)
        profit = [[0]*(n+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(n):
                profit[i][j] = _maxSubArray(nums[i:j+1])

        f = [[-65535]*(k+1) for _ in range(n+1)]
        for i in range(0, k+1):
            f[0][i] = -65535
        for i in range(1, n+1):
            f[i][0] = 0
        f[0][0] = 0
        for i in range(1, n+1):    
            for j in range(1, k+1):
                for x in range(j - 1, i):
                    f[i][j] = max(f[i][j], f[x][j-1] + profit[x][i-1])
        return f[n][k]
solution = Solution()
print solution.maxKSubArrays([1,2,3],1)
print solution.maxKSubArrays([-1,4,-2,3,-2,3], 2)
