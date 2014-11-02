class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        n = len(height)
        if n == 0:
            return 0
        elif n == 1:
            return height[0]
        stack = []
        mx = 0
        for i in range(n):
            if len(stack) == 0 or height[stack[-1]] <= height[i]:
                stack += [i]
            else:
                mx = max(mx, height[stack[0]] * i)
                while len(stack) > 0 and height[stack[-1]] >= height[i]:
                    j = stack.pop()
                    if len(stack) > 0:
                        mx = max(mx, height[j]*(i - stack[-1] - 1))
                    else:
                        mx = max(mx, height[j]*(i - j))
                    print height[j], i-j, mx
                stack += [i]
        mx = max(mx, height[stack[0]]*n)
        print stack
        for i in range(1, len(stack)):
            j = stack[i]
            mx = max(mx, height[j]*(n - stack[i-1] - 1))
            print height[j], n - stack[i-1], mx
        return mx
solution = Solution()
print solution.largestRectangleArea([4,2]) == 4
print solution.largestRectangleArea([1]) == 1
print solution.largestRectangleArea([1, 1]) == 2
print solution.largestRectangleArea([2, 1, 2]) == 3
print solution.largestRectangleArea([5, 4, 1, 2]) == 8
print solution.largestRectangleArea([4,2,0,3,2,5]) == 6
print solution.largestRectangleArea([3,6,5,7,4,8,1,0]) == 20
