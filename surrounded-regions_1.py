class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        row = len(board)
        if row == 0:
            return
        col = len(board[0])
        for i in range(row):
            self.check(board, i, 0, row, col)
            if col > 1:
                self.check(board, i, col - 1, row, col)
        for j in range(1, col):
            self.check(board, 0, j, row, col)
            if row > 1:
                self.check(board, row - 1, j, row, col)
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] == 'X'
                if board[i][j] == '1'
                    board[i][j] == 'O'
    def check(self, vec, i, j, row, col):
        if vec[i][j] == 'O':
            vec[i][j] == '1'
            if i > 1:
                self.check(vec, i - 1, j, row, col)
            if j > 1:
                self.check(vec, i, j - 1, row, col)
            if i + 1 < row:
                self.check(vec, i + 1, j, row, col)
            if j + 1 < col:
                self.check(vec, i, j + 1, row, col)
