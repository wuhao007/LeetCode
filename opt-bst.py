import sys
def opt_bst(p, n):
    e = [[0] * (n) for _ in range(n)] 
    root = [[-1] * (n) for _ in range(n)] 
    for i in range(n):
        e[i][i] = p[i]
    for L in range(2, n + 1):
        for i in range(0, n - L + 1):
            j = i + L - 1
            e[i][j] = sys.maxint
            for r in range(i, j + 1):
                left = e[i][r - 1] if r > i else 0
                right = e[r + 1][j] if r < j else 0
                t = left + right + sum(p[i : j + 1])
                if t < e[i][j]:
                    e[i][j] = t
                    root[i][j] = r
    return e, root
#print opt_bst([0.05, 0.2, 0.1, 0.3, 0.15, 0.05, 0.15], 7)
print opt_bst([0.25, 0.2, 0.05, 0.2, 0.3], 5)
