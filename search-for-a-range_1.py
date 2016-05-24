class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, n - 1
        ret = [2, -1]
        while i + 1 < j:
            mid = i + (j - i) / 2
            if nums[mid] < target:
                i = mid
            else:
                j = mid
        if nums[i] == target:
            ret[0] = i
        elif nums[j] == target:
            ret[0] = j
        else:
            ret[0] = -1
        
        i, j = 0, n - 1
        while i + 1 < j:
            mid = i + (j - i) / 2
            if target < nums[mid]:
                j = mid
            else:
                i = mid
        if nums[j] == target:
            ret[1] = j
        elif nums[i] == target:
            ret[1] = i
        else:
            ret[1] = -1

        return ret
