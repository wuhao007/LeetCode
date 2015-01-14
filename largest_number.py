def largestNumber(num):
    def num_str(x, y):
        m = len(x)
        n = len(y)
        x, y = x + y, y + x
        for i in range(m + n):
            if x[i] == y[i]:
                i += 1
            else:
                return ord(y[i]) - ord(x[i])

    return ''.join(sorted(map(lambda x : str(x), num), cmp = num_str))
print largestNumber([3, 30, 34, 5, 9])
print largestNumber([121,12])
