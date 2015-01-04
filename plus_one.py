def AddWithoutArithmetic(num1, num2):
    if num2 == 0: 
        return num1
    return AddWithoutArithmetic(num1 ^ num2, (num1 & num2) << 1)

def plusOne(digits):
    if digits == None or len(digits) == 0:
        return digits

    for i in range(len(digits) - 1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] = AddWithoutArithmetic(digits[i], 1)
            return digits
    ret = [0] * len(digits)
    return ret
print plusOne([3,9])
