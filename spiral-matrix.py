class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if matrix == []:
            return []
        else:
            result = []
            m = len(matrix)
            n = len(matrix[0])

            for i in range(n-1):
                result += [matrix[0][i]]

            if m <= 1:
                result += [matrix[0][n-1]]
            else:
                for i in range(m-1):
                    result += [matrix[i][n-1]]

                if n <= 1:
                    result += [matrix[m-1][0]]
                else:
                    for i in range(n-1, 0, -1):
                        result += [matrix[m-1][i]]

                    for i in range(m-1, 0, -1):
                        result += [matrix[i][0]]

            new_matrix = []
            for i in range(1, m-1):
                if matrix[i][1:n-1] != []:
                    new_matrix += [matrix[i][1:n-1]]

            return result + self.spiralOrder(new_matrix)
solution = Solution()
solution.spiralOrder([ [1],[2],[3], [4]  ])
