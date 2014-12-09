class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
	s = 0
        inverted_list = {0:-1}
        for i in range(len(nums)):
            s += nums[i]
            if s in inverted_list:
                return [inverted_list[s] + 1, i]
            else:
                inverted_list[s] = i
        return [-1, -1]
solution = Solution()
print solution.subarraySum([-4,5,-4,5,-4,5,-4,5,-4,5,-4,5,-4,5,-4,5,-4,5,-1000])
