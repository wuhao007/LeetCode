from sys import stdin, stdout
userinput = stdin.readline()
print userinput
nums = map(lambda x : int(x), userinput.split())
mx = nums[0]
mn = nums[0]
for num in nums:
    if num > mx:
        mx = num
    if num < mn:
        mn = num
stdout.write(str(mx) + ' ' + str(mn))
