string = "i am boy"
left = 0
right = len(string) - 1
while left < right:
    string[left], string[right] = string[right], string[left]
print string
