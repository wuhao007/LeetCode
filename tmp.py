class Solution:
    def solveSudoku(self, board):
        self.solve(board)
        
    def solve(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for k in range(1, 10):
                        c = chr(ord('0') + k)
                        if self.isValid(board, i, j, c):
                            board[i][j] = c
                            if self.solve(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True
    
    def isValid(self, board, i, j, c):
        for row in range(9):
            if board[row][j] == c:
                return False
        for col in range(9):
            if board[i][col] == c:
                return False
        rs = i / 3 * 3
        cs = j / 3 * 3
        for row in range(rs, rs + 3):
            for col in range(cs, cs + 3):
                if board[row][col] == c:
                    return False
        return True
