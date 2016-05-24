class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        used1 = [[0] * 9 for _ in range(9)]
        used2 = used1[:][:]
        used3 = used1[:][:]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != '.':
                    num = ord(board[i][j]) - ord('0') - 1
                    k = i / 3 * 3 + j / 3
                    if used1[i][num] or used2[j][num] or used3[k][num]:
                        return False
                    used1[i][num] = used2[j][num]  = used3[k][num] = 1
        return True
