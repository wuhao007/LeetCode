class Solution:
    """
    @param A: An integer array.
    @param k: a positive integer (k <= length(A))
    @param target: integer
    @return an integer
    """
    def solutionKSum(self, A, k, target):
        # write your code here
        n = len(A)
        f = [[[0] * (target + 1) for j in range(k + 1)] for i in range(n)]
        f[0][0][0] = 1
        f[0][1][A[0]] = 1
        for i in range(1, n):
            print i
            for j in range(min(i + 1, k) + 1):
                #print j, A[j - 1]
                for t in range(target + 1):
                    if i > 0:
                        f[i][j][t] += f[i - 1][j][t]
                        if j > 0 and t >= A[i]:    
                            f[i][j][t] += f[i - 1][j - 1][t - A[i]]
                    print i, j, t, f[i][j][t]
        return f[n - 1][k][target]   
solution = Solution()
print solution.solutionKSum([1,2,3,4], 2, 5)
