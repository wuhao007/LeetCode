class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        
        for row in board:
            s = set([])
            for x in row:
                if x == '.':
                    continue
                elif x in s:
	            print 1, x, s
                    return False
                else:
                    s.add(x)
            
        for j in range(len(board[0])):
            s = set([])
            for i in range(len(board)):
                if board[i][j] == '.':
                    continue
                elif board[i][j] in s:
	            print 2, board[i][j], s
                    return False
                else:
                    s.add(board[i][j])
                    
        for i in range(3):
            bi = i*3
            for j in range(3):
                bj = j*3
                s = set([])
                for k in range(3):
                    for l in range(3):
                        if board[bi + k][bj + l] == '.':
                            continue
                        elif board[bi + k][bj + l] in s:
	                    print 3, board[bi+k][bj+l], s
                            return False
                        else:
                            s.add(board[bi + k][bj + l])
        return True
solution = Solution()
solution.isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])
