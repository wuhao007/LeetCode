f = open('A-large.in', 'r')
T = int(f.readline())

def guarantee(C, D, V, denominations):
    f = [[False for v in range(V + 1)] for d in range(D + 1)]
    f[0][0] = True
    for i in range(D + 1):
        for j in range(V + 1):
            if j == 0:
                f[i][j] = True
            elif i == 0:
                f[i][j] = False
            else:
                f[i][j] = f[i][j] or f[i - 1][j]
                if j - A[i - 1] >= 0:
                    f[i][j] = f[i][j] or f[i-1][j - A[i - 1]]
    count = 0
    for j in range(V + 1):
        flag = False
        for i in range(D + 1):
            if f[i][j]:
                flag = True
                break
        if not flag:
            pass
            
                
for t in range(T):
    C, D, V = map(lambda x : int(x), f.readline().split())
    denominations = map(lambda x : int(x), f.readline().split())
    print 'Case #' + str(t+1) + ': ' + str(guarantee(C, D, V, denominations))
f.close()
