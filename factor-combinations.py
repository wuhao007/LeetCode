import math
class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        facts = []
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                facts += [i, n / i]
        facts.sort()
        m = len(facts)
        def dfs(path, result, pos, p):
            print path, p
            if p == 1:
                result += [path[:]]
            for i in range(pos, m):
                if i != pos and facts[i] == facts[i - 1]:
                    continue
                a = facts[i]
                if a > p:
                    break
                elif p % a == 0:
                    path += [a]
                    dfs(path, result, i, p / a)
                    path.pop()
        if n <= 1:
            return []
        result = []
        dfs([], result, 0, n)
        return result

solution = Solution()
print solution.getFactors(12)
