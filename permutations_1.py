class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.permuteRecursive(nums, 0, result)
    def permuteRecursive(self, nums, begin, result):
        if begin >= len(nums):
            result.append(nums[:])
            return
        for i in range(begin, len(nums)):
            nums[begin], nums[i] = nums[i], nums[begin]
            self.permuteRecursive(nums, begin + 1, result)
            nums[begin], nums[i] = nums[i], nums[begin]
        
