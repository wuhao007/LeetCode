class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows < 0:
            return
        row = []
        for i in range(numRows):
            row += [1]
            for j in range(i - 1, 0, -1):
                row[j] = row[j - 1] + row[j]
            print row
        for i in range(numRows - 1, 0, -1):
            row.pop() 
            for j in range(1, i):
                row[j] = row[j] - row[j - 1]
            print row
solution = Solution()
solution.generate(8)
