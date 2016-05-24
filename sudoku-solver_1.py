class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board == None or len(board) == 0:
            return
        self.solve(board)
    def solve(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    for k in range(1, 10):
                        c = chr(k + ord('0'))
                        if self.isValid(board, i, j, c):
                            board[i][j] = c
                            if self.solve(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False

    def isValid(self, board, i, j, c):
        for row in range(9):
            if board[row][j] == c:
                return False
        for col in range(9):
            if board[i][col] == c:
                return False
        for row in range(i / 3 * 3, i / 3 * 3 + 3):
            for col in range(j / 3 * 3, j / 3 * 3 + 3): 
                return False
        return True
