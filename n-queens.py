class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):

        def dfs(matrix, level, result):
            n = len(matrix)
            if level >= n:
                result += [matrix]
                return 1
            else:
                if True in matrix[level]:
                    s = 0
                    for i in range(n):
                        if matrix[level][i]:
                            new_matrix = [row[:] for row in matrix]
                            new_matrix[level] = "."* i + "Q" + "." *(n-i-1)
                            for j in range(level + 1, n):
                                new_matrix[j][i] = False
                                if 0 <= (i+j-level) < n:
                                    new_matrix[j][i+j-level] = False
                                if 0 <= (i-j+level) < n:
                                    new_matrix[j][i-j+level] = False
                            s += dfs(new_matrix, level + 1, result)
                    return s
                else:
                    return 0
        
        matrix = []
        for i in range(n):
            matrix += [[True]*n]
        result = []
        dfs(matrix, 0, result) 
        return result
solution = Solution()
print solution.solveNQueens(2)
