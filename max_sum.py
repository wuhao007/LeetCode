def max_sum(A):
    n = len(A)
    f = A[:]
    for i in range(1, n):
        f[i] += f[i - 1] 
    f.sort()
    mn = 65535
    for i in range(1, n):
        mn = min(mn, abs(f[i] - f[i - 1]))
    return mn
print max_sum([2, -4, 6, -3, 9])
