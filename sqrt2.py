def sqrt(x):
    k = 0
    while x > 2 ** (2 * k):
        k += 1
    l = float(2 ** (k - 1))
    r = float(2 ** k)
    while l < r:
        mid = l + (r - l) / 2
        value = mid * mid
        if abs(value - x) < 0.00001:
            return mid
        elif x < value:
            r = mid
        else:
            l = mid
    return -1
print sqrt(50000000)
