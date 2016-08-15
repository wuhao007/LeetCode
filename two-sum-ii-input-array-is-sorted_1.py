class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        indice = [0] * 2
        if numbers == None or len(numbers) < 2:
            return indice
        left, right = 0, len(numbers) - 1
        while left < right:
            v = numbers[left] + numbers[right]
            if v == target:
                return [left + 1, right + 1]
            elif v > target:
                right -= 1
            else:
                left += 1
        return indice    
