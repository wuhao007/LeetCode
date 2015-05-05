f = open('A-large.in', 'r')
T = int(f.readline())

def CounterCulture(N):
    i = int(N)
    count = 1
    while i != 0:
        i_str = str(i)
        if i_str[-1] != 0:
            reverse = int(i_str[::-1]) 
            if reverse < i:
                i = reverse 
                count += 1
            else:
                i -= 1
                count += 1
        else:
            i -= 1
            count += 1
    return count 
        

for t in range(T):
    N = f.readline().strip()
    print 'Case #' + str(t+1) + ': ' + str(CounterCulture(N))
f.close()
