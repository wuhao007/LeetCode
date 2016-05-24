class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        index = n - 1
        while index > 0:
            if nums[index - 1] < nums[index]:
                break
            index -= 1
        if index == 0:
            reverseSort(nums, 0, n - 1)
        else:
            val = nums[index - 1]
            j = n - 1
            while j >= index:
                if nums[j] > val:
                    break
                j -= 1
            nums[j], nums[index - 1] = nums[index - 1], nums[j]
            reverseSort(nums, index, n - 1)
    def reverseSort(self, nums, start, end):
        if start > end:
            return
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1       
