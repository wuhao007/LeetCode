class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n = len(s)
        result = [[] for i in range(n + 1)]
        pair = [[False] * n for i in range(n)]
        result[0] += [[]]
        for i in range(n):
            for left in range(i + 1):
                if s[left] == s[i] and (i <= (left + 1) or pair[left+1][i-1]):
                    pair[left][i] = True
                    string = s[left:i+1]
                    for r in result[left]:
                        result[i + 1] += [r[:] + [string]]
        print result
        return result[n]
solution = Solution()
print solution.partition("aab")
