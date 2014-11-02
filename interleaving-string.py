class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        m = len(s1)
        n = len(s2)
        if m == 0:
            return s2 == s3
        if n == 0:
            return s1 == s3
        matrix = [[False]*(n+1) for i in range(m+1)]
        matrix[0][0] = True
        print matrix 
        for i in range(1, m+1):
            if matrix[i-1][0] and s1[i-1] == s3[i-1]:
                matrix[i][0] = True
        for j in range(1, n+1):
            if matrix[0][j-1] and s2[j-1] == s3[j-1]:
                matrix[0][j] = True
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j] and s1[i-1] == s3[i+j-1]:
                    matrix[i][j] = True
                elif matrix[i][j-1] and s2[j-1] == s3[i+j-1]:
                    matrix[i][j] = True
                else:
                    matrix[i][j] = False
                    
        return matrix[m][n]
solution = Solution()
print solution.isInterleave('a','b','ab')
