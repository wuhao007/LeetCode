f = open('A-large.in', 'r')
T = int(f.readline())

for t in range(T):
    N = int(f.readline())
    m = map(lambda x : int(x), f.readline().split())
    first = 0
    mx_gap = 0
    for i in range(N - 1):
        gap = m[i] - m[i + 1]
        if gap  > 0:
            first += gap
        mx_gap = max(gap, mx_gap)
    speed = mx_gap / 10.0
    second = 0
    for i in range(N - 1):
        second += min(m[i], speed * 10)
        
     
    print 'Case #' + str(t+1) + ': ' + str(first) + ' ' + str(int(second)) 
f.close()
