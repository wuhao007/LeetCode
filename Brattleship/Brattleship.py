f = open('A-large.in', 'r')
T = int(f.readline())

def guarantee(R, C, W):
    num = C / W * R
    if C % W > 0:
        return num + W
    else:
        return num + W - 1
for t in range(T):
    R, C, W = map(lambda x : int(x), f.readline().split())
    print 'Case #' + str(t+1) + ': ' + str(guarantee(R, C, W))
f.close()
