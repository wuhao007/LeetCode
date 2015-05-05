f = open('D-small-attempt2.in', 'r')
T = int(f.readline())



def winner(X, R, C):
    if (R * C) % X != 0:
        return 'RICHARD'
    if X == 1:
        return 'GABRIEL'
    elif X == 2:
        return 'GABRIEL'
    elif X == 3:
        if R < 2 or C < 2:
            return 'RICHARD'
        else:
            return 'GABRIEL'
    elif X == 4:
        if (R == 4 and C >= 3) or (R >= 3 and C == 4):
            return 'GABRIEL'
        else:
            return 'RICHARD'
    
for t in range(T):
    X, R, C = map(lambda x : int(x), f.readline().split())
    print 'Case #' + str(t+1) + ': ' + winner(X, R, C)
f.close()
