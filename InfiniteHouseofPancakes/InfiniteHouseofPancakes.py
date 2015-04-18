f = open('A-large.in', 'r')
T = int(f.readline())

def how_quickly(D, P):
    P.sort()
    def binary_insert(n):
        l = 0
        r = len(P) - 1
        while l + 1 < r:
            m = l + (r - l) / 2
            if P[m] == n:
                l = m
            elif P[m] < n:
                l = m
            elif n < P[m]:
                r = m
        if P[r] <= n:
            P.insert(r + 1, n)
        elif P[l] <= n:
            P.insert(l + 1, n)
        else:
            P.insert(l, n)
        
    def special():
        num = P.pop()
        a = num / 2
        b = num - a
        binary_insert(a)
        binary_insert(b)
        
        
    
    return 0

for t in range(T):
    D = int(f.readline())
    P = map(lambda x : int(x), f.readline().split())
    print 'Case #' + str(t+1) + ': ' + str(how_quickly(D, P))
f.close()
