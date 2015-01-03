class Solution:
    def count(self, coins, money):
        n = len(coins)
        def dfs(money, path, index, memory):
            if money in memory:
                return memory[money][0]
            elif money == 0:
                return 0
            else:
                mn = 65535
                coin = -1
                for i in range(index, n):
                    if coins[i] > money:
                        break
                    path += [coins[i]]
                    number = dfs(money - coins[i], path, i, memory)
                    if number + 1 < mn:
                        mn = number + 1
                        coin = coins[i]
                    path.pop()
                memory[money] = (mn, coin)
                return memory[money][0]
        coins.sort()
        memory = {}
        dfs(money, [], 0, memory)
        ret = []
        while money > 0:
            ret += [memory[money][1]]
            money -= memory[money][1]
        return ret

solution = Solution()
print solution.count([1,2,3], 1)
print solution.count([1,2,3], 2)
print solution.count([1,2,3], 3)
print solution.count([1,2,3], 4)
print solution.count([1,2,3], 5)
print solution.count([1,2,3], 6)
print solution.count([1,2,3], 7)
print solution.count([1,2,3], 8)
print solution.count([1,2,3], 9)
print solution.count([1,2,3], 10)
print solution.count([1,2,3,5], 100)
