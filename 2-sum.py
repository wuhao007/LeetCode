class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        numbers.sort()
        n = len(numbers)
        left = 0
        right = n - 1
        result = []
        while left < right:
            s = numbers[left] + numbers[right]
            if s > target:
                right -= 1
            elif s < target:
                left += 1
            else:
                result += [left+1, right+1]
        return result
s = Solution()
print s.twoSum([2,7,11,15],9)
