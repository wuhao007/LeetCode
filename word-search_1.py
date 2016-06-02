class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for y in range(len(board)):
            for x in range(len(board[y])):
                if self.recur(board, y, x, list(word), 0):
                    return True
        return False
    def recur(self, board, y, x word, i):
        if i == len(word):
            return True
        if x < 0 or y < 0 or y >= len(board) or x >= len(board[y]): 
            return False
        if board[y][x] != word[i]:
            return False
        board[y][x] ^= 256
        boolean result = self.recur(board, y, x + 1, word, i + 1) or self.recur(board, y, x - 1, word, i + 1) or self.recur(board, y + 1, x, word, i + 1) or self.recur(board, y - 1, x, word, i + 1)
        board[y][x] ^= 256
        return result
