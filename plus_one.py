def AddWithoutArithmetic(num1, num2):
    if num2 == 0: 
        return num1
    sum = num1 ^ num2
    carry = (num1 & num2) << 1
    return AddWithoutArithmetic(sum,carry)
print AddWithoutArithmetic(39, 1)
