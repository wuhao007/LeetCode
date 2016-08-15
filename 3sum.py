def threeSum(self, numbers):
        # write your code here
        numbers.sort()
        res = []
        length = len(numbers)
        for i in range(length - 2):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            target = -numbers[i]
            left, right = i + 1, length - 1
            while left < right:
                if numbers[left] + numbers[right] == target:
                    res.append([numbers[i], numbers[left], numbers[right]])
                    right -= 1
                    left += 1
                    while left < right and numbers[left] == numbers[left - 1]:
                        left += 1
                    while left < right and numbers[right] == numbers[right + 1]:
                        right -= 1
                elif numbers[left] + numbers[right] > target:
                    right -= 1
                else:
                    left += 1
            return res
