class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        def largestRectangleArea(height):
            if height == []:
                return 0
            n = len(height)
            stack = [[0,0]]
            mx = 0
            height_mx = 0
            for i in range(1, n):
                if height[i] > height[stack[-1][1]]:
                    stack += [[i, i]]
                elif height[i] == height[stack[-1][1]]:
                    stack[-1][1] = i
                else:
                    s = 0
                    while stack != [] and height[i] < height[stack[-1][1]]:
                        node = stack.pop()
                        mx = max(mx, height[node[1]] * (i - node[0]))
                        s = node[0]
                    stack += [[s,i]]
            while stack != []:
                node = stack.pop()
                mx = max(mx, height[node[1]] * (n - node[0]))
            return mx
            
        def generateHeight(j, matrix):
            height = []
            k = j
            for i in range(len(matrix)):
                k = j
                while k < len(matrix[i]) and matrix[i][k] == '1':
                    k += 1
                height += [k-j]
            print height
            return height
            
        if len(matrix) < 1:
            return 0
        if len(matrix[0]) < 1:
            return 0
        area_mx = 0    
        j = 0
        for j in range(len(matrix[0])):
            area_mx = max(area_mx, largestRectangleArea(generateHeight(j, matrix)))
        return area_mx
solution = Solution()
print solution.maximalRectangle(["01101","11010","01110","11110","11111","00000"])
"01101"
"11010"
"01110"
"11110"
"11111"
"00000"
