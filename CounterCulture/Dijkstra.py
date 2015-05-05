f = open('A-small-attempt0.in', 'r')
T = int(f.readline())

def CounterCulture(N):
    length = len(N)
    if length == 1:
        return int(N)
    else:
        if N[0] == '1':
            return 1 + int(N[1:]) + CounterCulture('9' * (length - 1))
        else:
            if N[-1] == '0':
                return 1 + CounterCulture(str(int(N)-1))
            else:
                return int(N[-1]) + CounterCulture('1' + N[::-1][1:])
        

for t in range(T):
    N = f.readline().strip()
    print 'Case #' + str(t+1) + ': ' + str(CounterCulture(N))
f.close()
