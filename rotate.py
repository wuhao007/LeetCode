input: "12345"
int: 3
Left rotate 3 position

output: 45123

def rotate_str(string, n):
    str_len = len(string)
    if str_len <= 1:
        return string
    n = n % str_len
    rst = string
    for _ in range(n):
        rst = rst[1:] + rst[0]
    return rst
    
def rotate_str2(string, n):
    str_len = len(string)
    if str_len <= 1:
        return string
    n = n % str_len
    return string[n:] + string[:n]


"123 45"
 321 54
 45 123
 
    
def rotate_str3(string, n):
    str_len = len(string)
    if str_len <= 1:
        return string
    n = n % str_len
    left = 0
    right = n - 1
    while left < right:
        string[left], string[right] = string[right], string[left]
        left += 1
        right -= 1
    left = n
    right = str_len - 1
    while left < right:
        string[left], string[right] = string[right], string[left]
        left += 1
        right -= 1
    left = 0
    right = str_len - 1
    while left < right:
        string[left], string[right] = string[right], string[left]
        left += 1
        right -= 1
    return string
"123 45"
 |   |   
"423 15"
"453 12"

def rotate_str3(string, n): 
`   if n == 0:
        return string
    str_len = len(string)
    if str_len <= 1:
        return string
    n = n % str_len
    i = 0
    while i < min(n, str_len - n):
        string[i], string[i + n] = string[i + n], string[i]
        i += 1
    rotate_str(string[index:], n - min(n, str_len - n))
    return string
