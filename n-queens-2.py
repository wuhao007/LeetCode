class Solution:
    """
    Get all distinct N-Queen solutions
    @param n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        def _drawChessBoard(cols):
            n = len(cols)
            chessboard = []
            for i in range(n):
                line = ''
                for j in range(n):
                    if cols[i] == j:
                        line += 'Q'
                    else:
                        line += '.'
                chessboard += [line]
            return chessboard
            
        def _isValid(cols, col):
            row = len(cols)
            for i in range(row):
                if col == cols[i]:
                    return False
                elif i + cols[i] == row + col:
                    return False
                elif i - cols[i] == row - col:
                    return False
            return True
                    
        def _search(n, cols, result):
            if len(cols) == n:
                result += [_drawChessBoard(cols)]
            else:
                for col in range(n):
                    if _isValid(cols, col):
                        _search(n, cols + [col], result)
            
        if n <= 0:
            return []
        
        result = []
        _search(n, [], result)

        return result
solution = Solution()
print solution.solveNQueens(4)
            

