def count(coins, money):
    n = len(coins)
    f = [money] * (money + 1)
    f[0] = 0
    for i in range(n):
        for j in range(money + 1):
            if j >= coins[i]:
                f[j] = min(f[j], f[j - coins[i]] + 1) 
    return f[money]

print count([1,2,3], 4)
print count([2,3,5], 100)
