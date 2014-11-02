class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        if height == []:
            return 0
        height += [-1]
        n = len(height)
        stack = [0]
        mx = 0
        last = 0
        for i in range(1, n):
            if height[i] >= height[stack[-1]]:
                stack += [i]
            else:
                while stack != [] and height[stack[-1]] > height[i]:
                    it = stack.pop()
                    mx = max(mx, height[it]*(i-it))
                    last = it
                stack += [i]
        mx = max(mx, height[last] * (n-1))
        return mx
solution = Solution()
print solution.largestRectangleArea([5,4,1,2])
