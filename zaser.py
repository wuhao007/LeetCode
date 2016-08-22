# Hi I am Hao
# given a tic tac toe board, determine if the game is over or not
Class ttt():
    def __init__(self, n):
        self.row = [0] * n 
        self.col = [0] * n
        self.diag = 0
        self.antidiag = 0
        self.n = n
        '''
        o
         o
          o
        '''
    def over(self, board, i, j):

        toadd = 0
                if board[i][j] == 1:
                    toadd = 1
                else:
                    toadd = -1
                self.row[i] += toadd
                self.col[j] += toadd
                if i == j:
                    self.diag += toadd
                if i + j == self.n - 1:
                    self.antidiag += toadd
                
                if abs(self.row[i]) == self.n or abs(self.col[j]) == self.n or abs(self.diag) == self.n or abs(self.antidiag) == self.n:
                    return True
                cnt += abs(toadd)
                
        return True if cnt == self.n * self.n else False
