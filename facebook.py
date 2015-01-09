""// Given two strings of binary numbers, return the sum
a = "11"
b = "1"
a + b = c = "100"

def add(a, b):
    carry = 0
    ret = ''
    if len(a) < len(b):
        a,b = b,a
    pa = len(a) - 1
    pb = len(b) - 1
    while pb >= 0:
        s = int(a[pa]) + int(a[pb]) + carry
        carry = s / 2
        ret = str(s % 2) + ret
        pa -= 1
        pb -= 1
    while pa >= 0:
        s = int(a[pa]) + carry
        carry = s / 2
        ret = str(s % 2) + ret
        pa -= 1
    if carry > 0:
        ret = '1' + ret
    return ret
m = len(a)
n = len(b)
O(max(m, n))
O(max(m, n))
 
 
 
123 -> "one hundred and twenty three"
113
num = 123
n = 1000
table = {4:"thousrdd", 7:"millon", 10:"billion"}
num2eng = {1:"one",......9:'nine'}
num10eng = {1:"ten",.....9:'ninity'}
num100eng = {1:"ten",.....9:'ninity'}
100,000,000
def say_words(num):
    n = 1
    b = 0
    while n < num:
        b += 1    
        n *= 10
    n /= 10
    ret = ''
    while num > 0:
        bit = num / n
        num %= n
        if (b % 3) == 0:
            ret += num2eng[bit] + ' hundred ' + table[b] if b in table else ' '  
        elif (b % 3) == 2:
            ret += num10eng[bit] + ' '
        else: # b == 1
            ret += num2eng[bit]
            break
        n /= 10
        b -= 1
    return ret
123 11
