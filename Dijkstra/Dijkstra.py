f = open('C-large.in', 'r')
T = int(f.readline())

multiply_dict = {
    ('1','1'): '1',
    ('1','i'): 'i',
    ('1','j'): 'j',
    ('1','k'): 'k',
    ('i','1'): 'i',
    ('i','i'): '-1',
    ('i','j'): 'k',
    ('i','k'): '-j',
    ('j','1'): 'j',
    ('j','i'): '-k',
    ('j','j'): '-1',
    ('j','k'): 'i',
    ('k','1'): 'k',
    ('k','i'): 'j',
    ('k','j'): '-i',
    ('k','k'): '-1'
}

def multiply(a, b):
    def neg(ans):
        if ans[0] == '-':
            return ans[1]
        else:
            return '-' + ans[0]
    if a[0] == '-' and b[0] == '-':
        return multiply_dict[(a[1], b[1])]
    elif a[0] == '-' and b[0] != '-':
        return neg(multiply_dict[(a[1], b[0])])
    elif a[0] != '-' and b[0] == '-':
        return neg(multiply_dict[(a[0], b[1])])
    elif a[0] != '-' and b[0] != '-':
        return multiply_dict[(a[0], b[0])]

#print multiply('i', 'j') == 'k'
#print multiply('j', 'i') == '-k'
#print multiply('-k', 'j') == 'i'

for t in range(T):
    L, X = map(lambda x : int(x), f.readline().split())
    seq = f.readline()
    cur = '1'
    stagei = False
    stagek = False
    #test = [] 
    small = ''
    for x in range(X):
        for l in range(L):
            cur = multiply(cur, seq[l])
            #test += [cur]
            if (not stagei) and cur == 'i':
                stagei = True
            if stagei and cur == 'k':
                stagek = True
        if x == 0:
           small = cur
        if stagek:
            break
     
    ans = 'NO'
    if stagek:
        new = '1'
        for x in range(X):
            new = multiply(new, small) 
        if new == '-1':
            ans = 'YES'
    print 'Case #' + str(t+1) + ': ' + ans
f.close()
