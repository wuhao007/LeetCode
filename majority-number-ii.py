import random
class Solution:
    """
    @param nums: A list of integers
    @return: The majority number occurs more than 1/3
    """
    def majorityNumber(self, nums):
        # write your code here
        sz = len(nums)
        while len(nums) < sz:
            x = random.randrange(0, len(nums))
            y = random.randrange(0, len(nums))
            z = random.randrange(0, len(nums))
            sz = len(nums)
            if (nums[x] != nums[y]) and (nums[x] != nums[z]) and (nums[y] != nums[z]):
                nums.pop(x)
                nums.pop(y)
                nums.pop(z)
            print nums
        d = {}
        mx = 0
        result = nums[0]
        if len(nums) == 1:
            return nums[0]
        else:
            for n in nums:
                if n in d:
                    d[n] += 1
                else:
                    d[n] = 1
                if d[n] > mx:
                    mx = d[n]
                    result = n
        return result
solution = Solution()
print solution.majorityNumber([99,2,99,2,99,3,3])
