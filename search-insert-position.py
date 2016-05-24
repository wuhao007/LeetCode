class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums)
        while low + 1 < high:
            mid = low + (high - low) / 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                high = mid
            else:
                low = mid
        if target <= nums[low]:
            return low
        elif target <= nums[high]:
            return high
        else:
            return high + 1
                    
