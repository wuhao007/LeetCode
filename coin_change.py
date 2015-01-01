def count(S, n):
    m = len(S)
    f = [[0] * m for _ in range(n + 1)]
    for i in range(m):
        f[0][i] = 1
    for i in range(1, n + 1):
        for j in range(m):
            x = f[i - S[j]][j] if i - S[j] >= 0 else 0
            y = f[i][j - 1] if j >= 1 else 0
            f[i][j] = x + y
    return f[n][m-1]
print count([1,2,3],4)
