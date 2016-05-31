class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return 0  
        level = 0
        currentMax = 0
        i = 0
        nextMax = 0 
        while currentMax >= i:
            level += 1
            while i <= currentMax:
                nextMax = max(nextMax nums[i] + i)
                if nextMax >= n - 1:
                    return level
                i += 1
            currentMax = nextMax
        return 0
        
