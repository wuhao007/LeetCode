class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """
    def subarraySumClosest(self, nums):
        # write your code here
        s = [(0, nums[0])]
        n = len(nums)
        for i in range(1, n):
            s += [(i, s[i - 1][1] + nums[i])]
	print s
        s.sort(key = lambda x : x[1])
	print s
        mn = 65535
        ret = [-1, -1]
        for i in range(1, n):
            diff = s[i][1] - s[i - 1][1]
            if diff < mn:
                ret = [min(s[i - 1][0], s[i][0]) + 1, max(s[i - 1][0], s[i][0])]
        return ret
solution = Solution()
print solution.subarraySumClosest([-3,1,1,-3,5])
