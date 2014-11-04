class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        '''
        n = len(nums)
        mx = [0]*n
        mx[0] = nums[0]
        result = mx[0]
        for i in range(1, n):
            mx[i] = max(mx[i-1] + nums[i], nums[i])
            result = max(mx[i], result)
        return result
        '''
        n = len(nums)
        sigma = [0] + nums
	print sigma
        for i in range(1, n + 1):
            sigma[i] += sigma[i - 1]
	print sigma
        mx = 0
        mn = sigma[0]
        for i in range(1, n):
            mn = min(mn, sigma[i])
            mx = max(mx, sigma[i] - mn)
        return mx
solution = Solution()
print solution.maxSubArray([-2,2,-3,4,-1,2,1,-5,3])
