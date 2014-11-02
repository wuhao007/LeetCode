def addnum(l1, l2, c):
    if l1 == '' and l2 == '':
        if c > 0:
            return str(c)
        else:
            return '' 
    elif l1 == '':
        if c > 0:
            return addnum(str(c), l2, 0)
        else:
            return l2
    elif l2 == '':
        if c > 0:
            return addnum(l1, str(c), 0)
        else:
            return l1
    else:
        s = int(l1[-1]) + int(l2[-1]) + c
        if s < 10:
            return addnum(l1[:-1], l2[:-1], 0) + str(s)
        else:
            return addnum(l1[:-1], l2[:-1], s/10) + str(s%10)
            
def multiplyBit(a, b, c):
    if a == '':
        if c > 0:
            return str(c)
        else:
            return ''
    else:
        s = int(a[-1]) * int(b) + c
        return multiplyBit(a[:-1], b, s/10) + str(s%10)
num1 = '99999999999999999'
num2 = '0'
result = ''
for i in range(len(num2) - 1, -1, -1):
    result = addnum(multiplyBit(num1, num2[i], 0) + '0'*(len(num2)-1-i), result, 0)
print result
