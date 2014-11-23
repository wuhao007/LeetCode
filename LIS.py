'''
LIS(A)
    let n = length(A)
    let f[1..n] be new array
    for i = 1 to n
        f[i] = 1
    for i = 1 to n
        for j = 1 to i
            if A[j] <= A[i]
                f[i] = MAX(f[i], f[j] + 1)
    return MAX(f[1..n])

LCS-LENGTH(X, Y, m, n)
    let c[0..m, 0..n] be new table
    for i = 1 to m
        c[i,0] = 0
    for j = 0 to n
        c[0,j] = 0
    for i = 1 to m
        for j = 1 to n
            if X[i] == Y[j]
                c[i, j] = c[i -1, j -1] + 1
            else
                c[i, j] = max(c[i - 1, j], c[i, j - 1])
    return c[m, n]
BOTTOM-UP-CUT-ROD(p,n)
let r[0..n] be a new array
r[0] = 0
for j = 1 to n
    for i = 1 to j
        r[j] = max(r[j], p[i] + r[j - i])
return r[n]
'''
def BOTTOM_UP_CUT_ROD(p, n):
    r = [0] * (n + 1)
    for j in range(1, n + 1):
        for i in range(j):
            r[j] = max(r[j], p[i] + r[j - (i + 1)])
    print r
    return r[n]
print BOTTOM_UP_CUT_ROD([1, 5, 8, 9, 10, 17, 17, 20, 21], 9)
#a = [0.05, 0.2, 0.1, 0.3, 0.15, 0.05, 0.15]
#b = [2, 1, 2, 0, 2, 3, 1]
#n = len(a)
#total = 0
#for i in range(n):
#    total += a[i] * b[i]
#print total
