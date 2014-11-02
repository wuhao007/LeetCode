class Solution:
    """
    @param k: The number k.
    @return: The kth prime number as description.
    """
    def kthPrimeNumber(self, k):
        # write your code here
        import heapq
        key = [3, 5, 7]
        h = []
        for i in range(3):
            heapq.heappush(h, (key[i], i))
        value = key[0]
        while k > 0:
            value, level = heapq.heappop(h)
            while level < 3:
                new_value = key[level] * value
                heapq.heappush(h, (new_value, level))
                level += 1
            k -= 1
        return value
solution = Solution()
print solution.kthPrimeNumber(4)
