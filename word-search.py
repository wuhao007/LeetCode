class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word, i = 0, j = 0, k = 0):
        print board, word
        if word == '':
            return True
        m = len(board)
        n = len(board[0])
        if 0 <= i < m and 0 <= j < n:
            if board[i][j] == '$':
                return False
            elif board[i][j] == word[0]:
                board[i][j] = '$'
                if self.exist(board, word[1:], i+1, j) or self.exist(board, word[1:], i, j+1) or self.exist(board, word[1:], i-1, j) or self.exist(board, word[1:], i, j-1):
                    return True
                else:
                    board[i][j] = word[0]
                    return False
            else:
                return False
        else:
            return False
solution = Solution()
print solution.exist(["ab"], "ba")
