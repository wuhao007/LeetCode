class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        def solveSudoku(board, row, col):
	    #for i in board:
            #    print i
            if col >= 9:
                return solveSudoku(board, row+1, 0)
            if row >= 9:
                return False
            #print board[row][col]
            if board[row][col] == ".":
                bi = row/3*3
                bj = col/3*3
                #print bi, bj
                s = set([i for i in board[row]] + [board[i][col] for i in range(9)] + [board[bi + i][bj + j] for i in range(3) for j in range(3)])
                #print "======="
                #print s
                #print "======="

                #print [str(i) for i in range(9) if str(i) not in s]
                for j in [str(i) for i in range(9) if str(i) not in s]:
                    board[row] = board[row][:col] + j + board[row][col+1:]
                    if solveSudoku(board, row, col+1):
                        return True
                board[row] = board[row][:col] + '.' + board[row][col+1:]
                return False
            else:
                return solveSudoku(board, row, col+1)
        solveSudoku(board, 0, 0)
solution = Solution()
solution.solveSudoku(["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."])
