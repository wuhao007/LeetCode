class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        elem_num = len(nums)
        subset_num = 2 * elem_num
        subset_set = [[] for _ in range(subset_num)]
        for i in range(elem_num):
            for j in range(subset_num):
                if j >> i & 1 == 1:
                    subset_set[j].append(nums[i])
        return subset_set
         
