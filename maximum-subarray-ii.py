class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        # write your code here   
        n = len(nums)
        a = nums[:]
        aa = num[:]
        for i in range(1, n):
            a[i] = max(nums[i], a[i-1] + nums[i])
        aa[i] = max(a[i], aa[i-1])
        b = nums[:]
        bb = num[:]
        for i in range(n-2, -1, -1):
            b[i] = max(b[i+1] + nums[i], nums[i])
            bb[i] = max(b[i], bb[i+1])
        mx = -65535
        for i in range(n - 1):
            mx = max(aa[i]+b[i+1], mx)

        return mx

solution = Solution()
solution.maxTwoSubArrays()
