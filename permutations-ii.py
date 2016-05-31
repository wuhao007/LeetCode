class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        self.recursion(nums, 0, len(nums), res)
        return res
    def recursion(self, nums, i, j, res):
        if i == j - 1:
            res.append(nums[:])
        for k in range(i, j):
            if k != i and nums[k] == nums[k - 1]:
                continue
            nums[i], nums[k] = nums[k], nums[j]
            self.recursion(nums, i + 1, j, res)
            nums[i], nums[k] = nums[k], nums[j]
    
        
