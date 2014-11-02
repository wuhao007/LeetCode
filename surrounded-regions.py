class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        m = len(board)
        n = len(board[0])
        edge = []

        for i in range(1, m-1):
            if board[i][0] == 'O':
                edge += [(i, 0)]
            if board[i][n-1] == 'O':
                edge += [(i, n-1)]
        for i in range(n):
            if board[0][i] == 'O':
                edge += [(0, i)]
            if board[m-1][i] == 'O':
                edge += [(m-1, i)]

        def dfs(board, i, j, O, T):
            if (0 <= i < m) and (0 <= j < n):
                if board[i][j] == O:
                    board[i][j] = T
                    dfs(board, i+1, j, O, T)
                    dfs(board, i-1, j, O, T)
                    dfs(board, i, j+1, O, T)
                    dfs(board, i, j-1, O, T)

        print edge
        for node in edge:
            dfs(board, node[0], node[1], 'O', 'T')
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'
                    

board = [['X','X','X','X'],['X','O','O','X'],['X','X','O','X'],['X','O','X','X']]
solution = Solution()
solution.solve(board)
print board
