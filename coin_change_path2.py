def count(coins, money):
    n = len(coins)
    # f[i][j] [0...i) coins $j min number of coins
    f = [[money] * (money + 1) for _ in range(n)]
    for i in range(n):
        f[i][0] = 0
    for i in range(money + 1):
        if i % coins[0] == 0:
            f[0][i] = i / coins[0]
    for i in range(1, n):
        for j in range(money + 1):
            f[i][j] = min(f[i][j], f[i - 1][j])
            if j > coins[i]:
                f[i][j] = min(f[i][j], f[i - 1][j - coins[i]] + 1) 
    return min([f[i][money] for i in range(n)])

print count([1,2,3],4)
