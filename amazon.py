# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
matrix = []
res = [['0'] * n for _ in range(n)]
for i in range(n):
    row = raw_input().split()
    if len(row) != n:
        res = "ERROR"
        break
    matrix.append(row)
#print matrix
def printr(res):
    for row in res:
        print ' '.join(row)
    print
    
rowBegin, rowEnd, colBegin, colEnd = 0, n - 1, 0, n - 1
while rowBegin < rowEnd and colBegin < colEnd:
    c1 = matrix[rowBegin][colEnd]
    for j in range(colEnd - 1, colBegin - 1, - 1):
        res[rowBegin][j+1] = matrix[rowBegin][j]
    rowBegin += 1
    printr(res)
    
    c2 = matrix[rowEnd][colEnd]
    for i in range(rowEnd - 1, rowBegin - 1, -1):
        res[i+1][colEnd] = matrix[i][colEnd]
    res[rowBegin][colEnd] = c1
    colEnd -= 1
    printr(res)
    
    c3 = matrix[rowEnd][colBegin]
    for j in range(colBegin + 1, colEnd):
        res[rowEnd][j-1] = matrix[rowEnd][j]
    res[rowEnd][colEnd] = c2
    rowEnd -= 1
    printr(res)
    
    c4 = matrix[rowBegin][colBegin]
    for i in range(rowBegin + 1, rowEnd):
        res[i-1][colBegin] = matrix[i][colBegin]
    res[rowEnd][colBegin] = c3
    colBegin += 1
    printr(res)

