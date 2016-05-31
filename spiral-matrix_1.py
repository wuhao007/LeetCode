class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if len(matrix) == 0:
            return []
        rowBegin, rowEnd, colBegin, colEnd = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        while rowBegin <= rowEnd and colBegin <= colEnd:
            for j in range(colBegin, colEnd + 1):
                res.append(matrix[rowBegin][j])
            rowBegin += 1
            for i in range(rowBegin, rowEnd + 1):
                res.append(matrix[i][colEnd])
            colEnd -= 1
            if rowBegin <= rowEnd:
                for j in range(colEnd, colBegin - 1, -1):
                    res.append(matrix[rowEnd][j]
            colEnd -= 1
            for colBegin <= colEnd:
                for i in range(rowEnd, rowBegin - 1, -1):
                    res.append(matrix[i][colBegin]
            colBegin += 1
        return res
