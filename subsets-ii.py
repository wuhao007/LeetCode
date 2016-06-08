class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        totalset = []
        nums.sort()
        for i in range(len(nums)):
            count = 0
            while count + i < len(nums) and nums[count + i] == nums[i]:
                count += 1
            previousN = len(totalset)
            for k in range(previousN):
                instance = totalset[k]
                for j in range(count):
                    instance.append(nums[i])
                    totalset.append(instance)
            i += count
        return totalset     
