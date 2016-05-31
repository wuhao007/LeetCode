class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lastPos = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] + i >= lastPos:
                lastPos = i
        return lastPos == 0
