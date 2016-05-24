class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo, hi = 0, n - 1
        while lo < hi:
            mid = lo + (hi - lo) / 2
            if nums[mid] == target:
                return mid
            if nums[lo] < nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid
                else:
                    lo = mid
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid
                else:
                    hi = mid
        if nums[lo] == target:
            return lo
        elif nums[hi] == target:
            return hi
        else:
            return -1
                    
