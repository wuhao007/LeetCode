r = open('new_years_resolution_example_input.txt', 'r')
w = open('new_years_resolution_output.txt', 'w')
T = int(r.readline())
#print T
for i in range(T):
    GP, GC, GF = map(lambda x : int(x), r.readline().split())
    #print GP, GC, GF
    N = int(r.readline())
    #print N
    foods = [map(lambda x : int(x), r.readline().split()) for _ in range(N)]
    #print foods
    def helper(GP, GC, GF, index):
        if GP == GC == GF == 0:
            return True
        elif GP < 10 or GC < 10 or GF < 10:
            return False
        for i in range(index, N):
            if helper(GP - foods[i][0], GC - foods[i][1], GF - foods[i][2], i + 1):
                return True
        return False
    result = 'yes' if helper(GP, GC, GF, 0) else 'no'
    print "Case #" + str(i + 1) + ': ' + result
            
r.close()
w.close()
