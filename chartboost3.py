from sys import stdin, stdout
userinput = stdin.readline()
nums = map(lambda x : int(x), userinput.split())
n = len(nums)
left = 0
cur = 0
right = n - 1
while cur <= right:
    if nums[cur] == 0:
        nums[cur], nums[left] = nums[left], nums[cur]
        left += 1
        cur += 1
    elif nums[cur] == 1:
        cur += 1
    else:
        nums[cur], nums[right] = nums[right], nums[cur]
        right -= 1
stdout.write(str(nums))
