class Solution:
    def __init__(self):
        self.cnt = 0
    def dfs(self, matrix, parent, length):
        if length == 0:
            self.cnt += 1
        else:
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    if parent is not None:
                        if abs(parent[0] - i) == 2 and parent[1] == j:
                            continue
                        if parent[0] == i and abs(parent[1] - j) == 2:
                            continue
                        if abs(parent[0] - i) == 2 and abs(parent[0] - j) == 2:
                            continue
                    if matrix[i][j]:
                        matrix[i][j] = False
                        self.dfs(matrix, (i, j), length - 1)
                        matrix[i][j] = True
    def run(self, num):
        self.dfs([[True] * 3 for _ in range(3)], None, num) 
        return self.cnt
solution = Solution()
print solution.run(8)
