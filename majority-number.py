class Solution:
    """
    @param nums: A list of integers
    @return: The majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        def majorityNumberList(nums):
            n = len(nums)
            if n <= 1:
                return nums
            elif n == 2:
                if nums[0] == nums[1]:
                    return nums
                else:
                    return []
            else:
                l = majorityNumberList(nums[0:n/2]) 
                r = majorityNumberList(nums[n/2:n])
                l_len = len(l)
                r_len = len(r)
                if l_len == 0:
                    return r
                if r_len == 0:
                    return l
                if l[0] == r[0]:
                    return l + r
                elif l_len < r_len:
                    return r[l_len:]
                else:
                    return l[r_len:]
        return majorityNumberList(nums)

solution = Solution()
print solution.majorityNumber([1,1,1,1,2,2,2])
