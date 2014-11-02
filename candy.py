class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        n = len(ratings)
        if n == 1:
            return 1
        a = [1]*n
        total = 1
        for i in range(1, n):
            if ratings[i-1] < ratings[i]:
                a[i] = a[i-1] + 1
            total += a[i]

        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                if a[i] > a[i+1]:
                    continue
                else:
                    total = total - a[i] + a[i+1] + 1
                    a[i] = a[i+1] + 1
        return total
solution = Solution()
print solution.candy([4,2,3,4,1])
