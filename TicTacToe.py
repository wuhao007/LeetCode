class TicTacToe(object):
    def __init__(self, n):
        self.size = n
        self.current = 0
        self.col_counter = [0] * n
        self.col_queue = []
        self.row_counter = 0
        self.row_queue = [[] for _ in xrange(n)]
    def update(self, n, queue, counter, v):
        new_counter = 0 if n == 0 else counter + 1
        if len(queue) > 0 and queue[-1] == v:
            queue.pop()
        if new_counter >= self.size:
            queue.insert(0, self.current)  # might 
        return new_counter
    def next(self, n):
        self.col_counter[self.current % self.size] = self.update(n, self.col_queue, self.col_counter[self.current % self.size], self.current - self.size)
        self.row_counter = self.update(n, self.row_queue[self.current % self.size], self.row_counter, self.current - self.size ** 2)
        self.current += 1
        return 0 if len(self.col_queue) == 0 and len(self.row_queue[(self.current - 1) % self.size]) == 0 else 1
    
ttt = TicTacToe(3)
print [(x, ttt.next(x)) for x in [1, 0, 0] * 3 + [0] * 10]
print [(x, ttt.next(x)) for x in [1, 1, 1]  + [0] * 10]
