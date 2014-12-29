class Solution:
    """
    @param nums: A list of integers.
    @return: An integer denotes the middle number of the array.
    """
    def median(self, nums):
        # write your code here
        from random import shuffle
        shuffle(nums)
        def partition(lo, hi, nums):
            print lo, hi
            if lo >= hi:
                return (lo, hi)
            lt = lo
            gt = hi
            v = nums[lo]
            i = lo
            while i <= gt:
                if nums[i] < v:
                    nums[i], nums[lt] = nums[lt], nums[i]
                    lt += 1
                    i += 1
                elif nums[i] > v:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                else:
                    i += 1
            return (lt, gt)
        i = 0
        j = len(nums) - 1
        m = j / 2
        while i < j:
            lo, hi = partition(i, j, nums)
            #print nums, lo, hi
            if lo > hi:
                return -1
            elif lo <= m <= hi:
                return nums[m]
            elif hi < m:
                i = hi + 1
            elif m < lo:
                j = lo - 1
        return nums[i]
#solution = Solution()
#print solution.median([4,5,1,2,3])
#print solution.median([7,9,4,5])
#print solution.median([-4,5,-4,5,-4,5,-4,5,-4,5,-4,5,-4,5,-4,5,-4,5,-1000])
