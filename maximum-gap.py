class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        import sys, math
        mn = sys.maxint
        mx = -sys.maxint - 1
        for number in num:
            mn = min(mn, number)
            mx = max(mx, number)
        n = len(num)
        step = (mx - mn) / (n - 1.0)
        array = [None for i in range(n)]
        for number in num:
            k = int(math.floor((number - mn) / step))
            if array[k] is None:
                array[k] = [number, number]
            else:
                array[k] = [min(array[k][0], number), max(array[k][1], number)]
        gap = 0
        prev = array[0][1]
        for i in range(1, n):
            if array[i] is None:
                continue
            else:
                gap = max(gap, array[i][0] - prev)
                prev = array[i][1]
        return gap
                
solution = Solution()
print solution.maximumGap([1,2,5])
