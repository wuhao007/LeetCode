class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return [[i for i in range(1, k + 1)]] if k == n or k == 0 else map(lambda x: x + [n], self.combine(n - 1, k - 1)) + self.combine(n - 1, k)
