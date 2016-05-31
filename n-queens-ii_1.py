class Solution(object):
    occupiedCols = set()
    occupiedDiag1s = set()
    occupiedDiag2s = set()
    count = 0
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        totalNQueensHelper(0, n)
        return self.count
    def totalNQueensHelper(row, n):
        for col in range(n):
            diag1, diag2 = row + col, row - col
            if col in occupiedCols or diag1 in occupiedDiag1s or diag2 in occupiedDiag2s:
                continue
            if row == n - 1:
                self.count += 1
            else:
                occupiedCols.add(cols)
                occupiedCols.add(diag1)
                occupiedCols.add(diag2)
                self.totalNQueensHelper(row + 1, n)
                occupiedCols.remove(cols)
                occupiedCols.remove(diag1)
                occupiedCols.remove(diag2)
                
    
            
