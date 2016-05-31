class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        nQueens = ['.' * n for _ in range(n)]
        flag_col, flag_45, flag_135 = [True] * n, [True] * (2 * n - 1), [True] * (2 * n - 1)
        self.solve(res, nQueens, flag_col, flag_45, flag_135, 0, n)
        return res

    def solve(self, res, nQueens, flag_col, flag_45, flag_135, row, n):
        if row == n:
            res.append(nQueens[:][:])
            return
        for col in range(n):
            if self.isValid(nQueens, row, col, n):
                flag_col[col] = flag_45[row + col] = flag_135[n - 1 + row - col] = False
                nQueens[row][col] = 'Q'
                self.solve(res, nQueens, flag_col, flag_45, flag_135, row + 1, n)
                nQueens[row][col] = '.'
                flag_col[col] = flag_45[row + col] = flag_135[n - 1 + row - col] = True
