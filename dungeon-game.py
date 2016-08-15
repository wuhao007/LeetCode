class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        M, N = len(dungeon), len(dungeon[0])
        hp = [[sys.maxint] * (N + 1) for _ in range(M + 1)]
        hp[M][N - 1] = hp[M - 1][N] = 1
        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                need = min(hp[i + 1][j], hp[i][j + 1]) - dungeon[i][j]
                hp[i][j] = 1 if need <= 0 else need
        return hp[0][0]
